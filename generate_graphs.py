#!/usr/bin/env python3
"""
Graph Generation Script
Generates all experimental result graphs for both algorithms
"""

import os
import matplotlib.pyplot as plt
import numpy as np
from vm_scheduler_implementation import (
    measure_algorithm_performance, create_realistic_scenario, 
    solve_vm_scheduling
)
from datacenter_proximity_implementation import (
    measure_algorithm_performance as measure_dc_performance,
    create_realistic_datacenters, solve_datacenter_proximity
)

def generate_greedy_graphs():
    """Generate graphs for greedy algorithm."""
    print("Generating greedy algorithm graphs...")
    
    # Create output directory
    os.makedirs('experimental_results', exist_ok=True)
    
    # Generate performance data
    sizes = [10, 50, 100, 500, 1000, 2000]
    results = measure_algorithm_performance(sizes)
    
    sizes_array = np.array([r[0] for r in results])
    times_array = np.array([r[1] for r in results])
    
    # Create simplified performance dashboard with only 2 plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('VM Reservation Scheduling - Greedy Algorithm Performance Analysis', fontsize=16)
    
    # Plot 1: Scalability analysis
    theoretical_nlogn = sizes_array * np.log2(sizes_array)
    scale_factor = times_array[0] / theoretical_nlogn[0]
    theoretical_times = scale_factor * theoretical_nlogn
    
    ax1.loglog(sizes_array, times_array, 'bo-', linewidth=2, markersize=8, label='Measured')
    ax1.loglog(sizes_array, theoretical_times, 'r--', linewidth=2, alpha=0.8, label='O(n log n)')
    ax1.set_xlabel('Input Size (log scale)')
    ax1.set_ylabel('Execution Time (log scale)')
    ax1.set_title('Scalability Analysis (Log-Log Plot)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Sample scheduling result
    reservations = create_realistic_scenario()
    selected, rejected = solve_vm_scheduling(reservations)
    
    categories = ['Selected', 'Rejected']
    counts = [len(selected), len(rejected)]
    colors = ['lightgreen', 'lightcoral']
    
    bars = ax2.bar(categories, counts, color=colors, alpha=0.8)
    ax2.set_ylabel('Number of Reservations')
    ax2.set_title(f'Scheduling Result (Success Rate: {len(selected)/len(reservations):.1%})')
    
    for bar, count in zip(bars, counts):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
               str(count), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('experimental_results/VM_performance_dashboard.png', dpi=300, bbox_inches='tight')
    print("Created VM_performance_dashboard.png")
    
    # Create realistic scenario timeline
    create_timeline_visualization(selected, rejected, reservations)


def create_timeline_visualization(selected, rejected, all_reservations):
    """Create clean timeline visualization showing actual scheduling."""
    
    fig, ax = plt.subplots(figsize=(16, 8))
    
    # Sort reservations by start time
    all_sorted = sorted(all_reservations, key=lambda r: r.start_time)
    
    # Calculate time bounds
    min_hour = min(res.start_time.hour + res.start_time.minute/60 for res in all_reservations)
    max_hour = max(res.end_time.hour + res.end_time.minute/60 for res in all_reservations)
    x_min = max(7, min_hour - 0.5)
    x_max = min(23, max_hour + 0.5)
    
    # Plot reservations
    y_pos = 0
    y_labels = []
    
    for res in all_sorted:
        start_hour = res.start_time.hour + res.start_time.minute/60
        duration = (res.end_time - res.start_time).total_seconds() / 3600
        
        # Color based on selection status
        if res in selected:
            color = '#90EE90'
            edge_color = '#228B22'
        else:
            color = '#FFB6C1'
            edge_color = '#DC143C'
        
        ax.barh(y_pos, duration, left=start_hour, height=0.8, 
                color=color, alpha=0.8, edgecolor=edge_color, linewidth=2)
        
        # Add job name
        job_name = res.id.split('-')[-1]
        if duration > 0.3:
            ax.text(start_hour + duration/2, y_pos, job_name, 
                    ha='center', va='center', fontsize=9, weight='bold')
        
        # Y-axis label
        start_str = res.start_time.strftime("%H:%M")
        end_str = res.end_time.strftime("%H:%M")
        y_labels.append(f"{job_name} ({start_str}-{end_str})")
        y_pos += 1
    
    # Format timeline
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(-0.5, len(all_sorted) - 0.5)
    ax.set_xlabel('Time (24-hour format)', fontsize=12)
    ax.set_ylabel('VM Reservations', fontsize=12)
    ax.set_title(f'VM Reservation Scheduling Timeline\n'
                 f'Selected: {len(selected)} | Rejected: {len(rejected)} | '
                 f'Success Rate: {len(selected)/len(all_reservations):.1%}', 
                 fontsize=14, fontweight='bold')
    
    ax.set_yticks(range(len(all_sorted)))
    ax.set_yticklabels(y_labels, fontsize=8)
    ax.grid(True, alpha=0.3)
    
    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#90EE90', edgecolor='#228B22', label=f'Selected ({len(selected)})'),
        Patch(facecolor='#FFB6C1', edgecolor='#DC143C', label=f'Rejected ({len(rejected)})')
    ]
    ax.legend(handles=legend_elements, loc='upper right')
    
    plt.tight_layout()
    plt.savefig('experimental_results/VM_realistic_scenario_timeline.png', 
                dpi=300, bbox_inches='tight')
    print("Created VM_realistic_scenario_timeline.png")
    plt.close()


def generate_divide_conquer_graphs():
    """Generate graphs for divide and conquer algorithm."""
    print("\nGenerating divide & conquer algorithm graphs...")
    
    # Generate performance data
    sizes = [10, 50, 100, 500, 1000, 2000]
    dc_results, bf_results = measure_dc_performance(sizes)
    
    # Create simplified dashboard with only 2 plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('Datacenter Proximity Analysis - Divide & Conquer Performance', fontsize=16)
    
    # Plot 1: Log-scale comparison
    dc_sizes = np.array([r[0] for r in dc_results])
    dc_times = np.array([r[1] for r in dc_results])
    
    ax1.loglog(dc_sizes, dc_times, 'bo-', linewidth=2, markersize=8, label='Divide & Conquer')
    
    if bf_results:
        bf_sizes = np.array([r[0] for r in bf_results])
        bf_times = np.array([r[1] for r in bf_results])
        ax1.loglog(bf_sizes, bf_times, 'ro-', linewidth=2, markersize=8, label='Brute Force')
    
    # Add theoretical curves
    scale_dc = dc_times[0] / (dc_sizes[0] * np.log2(dc_sizes[0]))
    theoretical_dc = scale_dc * dc_sizes * np.log2(dc_sizes)
    ax1.loglog(dc_sizes, theoretical_dc, 'b--', alpha=0.6, label='O(n log n)')
    
    if bf_results:
        scale_bf = bf_times[0] / (bf_sizes[0] ** 2)
        theoretical_bf = scale_bf * bf_sizes ** 2
        ax1.loglog(bf_sizes, theoretical_bf, 'r--', alpha=0.6, label='O(n²)')
    
    ax1.set_xlabel('Input Size (log scale)')
    ax1.set_ylabel('Execution Time (log scale)')
    ax1.set_title('Scalability Analysis (Log-Log Plot)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Real datacenter analysis
    datacenters = create_realistic_datacenters()
    dc_result = solve_datacenter_proximity(datacenters, "divide_conquer")
    bf_result = solve_datacenter_proximity(datacenters, "brute_force")
    
    algorithms = ['Divide &\nConquer', 'Brute Force']
    comparisons = [dc_result.comparisons_made, bf_result.comparisons_made]
    colors = ['lightblue', 'lightcoral']
    
    bars = ax2.bar(algorithms, comparisons, color=colors, alpha=0.8)
    ax2.set_ylabel('Number of Comparisons')
    ax2.set_title(f'Real Datacenter Analysis\nClosest Pair: {dc_result.distance:.4f}°')
    
    # Add value labels on bars
    for bar, comp in zip(bars, comparisons):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                str(comp), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('experimental_results/datacenter_performance_dashboard.png', dpi=300, bbox_inches='tight')
    print("Created datacenter_performance_dashboard.png")
    
    # Create datacenter location visualization
    create_datacenter_map_visualization(datacenters, dc_result)


def create_datacenter_map_visualization(datacenters, result):
    """Create clean datacenter location visualization."""
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Get coordinates
    lons = [dc.longitude for dc in datacenters]
    lats = [dc.latitude for dc in datacenters]
    
    # Plot all datacenters
    ax.scatter(lons, lats, c='lightblue', s=80, alpha=0.8, 
              edgecolors='navy', linewidth=1, label='Datacenters')
    
    # Highlight closest pair
    closest_point1 = result.point1
    closest_point2 = result.point2
    
    ax.scatter([closest_point1[0]], [closest_point1[1]], c='red', s=200, 
              marker='D', edgecolors='darkred', linewidth=2, 
              label='Closest Point 1')
    
    ax.scatter([closest_point2[0]], [closest_point2[1]], c='yellow', s=250, 
              marker='*', edgecolors='orange', linewidth=2, 
              label='Closest Point 2')
    
    # Draw connecting line
    ax.plot([closest_point1[0], closest_point2[0]], 
           [closest_point1[1], closest_point2[1]], 
           'red', linewidth=3, alpha=0.8)
    
    # Format map
    ax.set_xlabel('Longitude (degrees)')
    ax.set_ylabel('Latitude (degrees)')
    ax.set_title(f'Global Datacenter Network\nClosest Pair Distance: {result.distance:.4f}°', 
                fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left')
    
    plt.tight_layout()
    plt.savefig('experimental_results/datacenter_map_analysis.png', dpi=300, bbox_inches='tight')
    print("Created datacenter_map_analysis.png")
    plt.close()


def main():
    """Generate all experimental graphs."""
    print("Generating All Experimental Result Graphs")
    print("=" * 50)
    
    try:
        generate_greedy_graphs()
        generate_divide_conquer_graphs()
        
        print(f"\nAll graphs generated successfully!")
        
    except Exception as e:
        print(f"Error generating graphs: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()