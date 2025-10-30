#!/usr/bin/env python3
"""
VM Reservation Scheduler 
Greedy Algorithm for Interval Scheduling Optimization

"""

from datetime import datetime, timedelta
from typing import List, Tuple
import time
import random
import numpy as np


class VMReservation:
    """Represents a VM reservation request."""
    
    def __init__(self, id: str, start_time: datetime, end_time: datetime, customer_id: str):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.customer_id = customer_id
    
    def to_interval(self) -> Tuple[float, float]:
        return (self.start_time.timestamp(), self.end_time.timestamp())
    
    def overlaps_with(self, other: 'VMReservation') -> bool:
        return not (self.end_time <= other.start_time or other.end_time <= self.start_time)


def greedy_interval_scheduling(intervals: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """Greedy algorithm for interval scheduling optimization."""

    if not intervals:
        return []
    
    # Phase 1: Sort by finish time - O(n log n)
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    # Phase 2: Greedy selection - O(n)
    selected = []
    last_finish = float('-inf')
    
    for start, end in sorted_intervals:
        if start >= last_finish:  # No overlap with previous selection
            selected.append((start, end))
            last_finish = end
    
    return selected


def solve_vm_scheduling(reservations: List[VMReservation]) -> Tuple[List[VMReservation], List[VMReservation]]:  
    # Convert to intervals
    intervals = [res.to_interval() for res in reservations]
    
    # Apply greedy algorithm
    selected_intervals = greedy_interval_scheduling(intervals)
    
    # Map back to reservations
    interval_to_reservation = {res.to_interval(): res for res in reservations}
    
    selected_reservations = [interval_to_reservation[interval] for interval in selected_intervals]
    selected_ids = {res.id for res in selected_reservations}
    rejected_reservations = [res for res in reservations if res.id not in selected_ids]
    
    return selected_reservations, rejected_reservations


def create_realistic_scenario() -> List[VMReservation]:
    """Create a realistic VM reservation scenario for testing."""
    base_date = datetime(2024, 1, 15, 0, 0)  # Start at midnight

    job_specs = [
        ("DataSync1", 8.0, 1.5),      # 8:00-9:30
        ("ReportGen", 8.5, 2.0),      # 8:30-10:30 (overlaps)
        ("ETLProcess", 9.0, 1.0),     # 9:00-10:00 (overlaps)
        ("BackupJob", 10.0, 1.5),     # 10:00-11:30
        ("Analytics1", 10.5, 2.0),    # 10:30-12:30 (overlaps)
        ("QuickTask1", 11.0, 0.5),    # 11:00-11:30 (overlaps)
        ("DataClean", 11.5, 1.0),     # 11:30-12:30
        ("MLTraining", 13.0, 3.0),    # 1:00-4:00 PM
        ("WebScrape", 13.5, 1.0),     # 1:30-2:30 PM (overlaps)
        ("DataMining", 14.0, 2.0),    # 2:00-4:00 PM (overlaps)
        ("QuickAnalysis", 15.0, 0.5), # 3:00-3:30 PM (overlaps)
        ("ReportGen2", 16.0, 1.5),    # 4:00-5:30 PM
        ("Validation", 16.5, 1.0),    # 4:30-5:30 PM (overlaps)
        ("FinalSync", 17.0, 0.5),     # 5:00-5:30 PM (overlaps)
        ("SystemMaint", 18.0, 2.0),   # 6:00-8:00 PM
        ("SecurityScan", 19.0, 1.5),  # 7:00-8:30 PM (overlaps)
        ("LogAnalysis", 20.0, 1.0),   # 8:00-9:00 PM
        ("Cleanup", 20.5, 1.0),       # 8:30-9:30 PM (overlaps)
    ]
    
    reservations = []
    for i, (job_name, start_hour, duration_hours) in enumerate(job_specs):
        start_time = base_date + timedelta(hours=start_hour)
        end_time = start_time + timedelta(hours=duration_hours)
        
        reservation = VMReservation(
            id=f"vm-{i+1:02d}-{job_name}",
            start_time=start_time,
            end_time=end_time,
            customer_id=f"customer-{(i % 8) + 1}"
        )
        reservations.append(reservation)
    
    return reservations


def measure_algorithm_performance(sizes: List[int], num_trials: int = 5) -> List[Tuple[int, float]]:
    """Measure algorithm performance for complexity validation."""

    results = []
    
    for n in sizes:
        times = []
        
        for _ in range(num_trials):
            # Generate random intervals
            intervals = []
            for _ in range(n):
                start = random.uniform(0, 100)
                duration = random.uniform(0.5, 5.0)
                end = start + duration
                intervals.append((start, end))
            
            # Measure execution time
            start_time = time.perf_counter()
            greedy_interval_scheduling(intervals)
            end_time = time.perf_counter()
            
            times.append(end_time - start_time)
        
        avg_time = sum(times) / len(times)
        results.append((n, avg_time))
        print(f"Size {n:4d}: {avg_time:.6f}s average")
    
    return results


def validate_complexity():
    """Validate O(n log n) complexity experimentally."""
    print("Validating O(n log n) complexity...")
    
    sizes = [10, 50, 100, 500, 1000, 2000]
    results = measure_algorithm_performance(sizes)
    
    # Calculate R² correlation with n log n
    sizes_array = np.array([r[0] for r in results])
    times_array = np.array([r[1] for r in results])
    
    # Theoretical n log n curve
    theoretical_nlogn = sizes_array * np.log2(sizes_array)
    scale_factor = times_array[0] / theoretical_nlogn[0]
    theoretical_times = scale_factor * theoretical_nlogn
    
    # Calculate R² correlation coefficient
    correlation_matrix = np.corrcoef(theoretical_times, times_array)
    r_squared = correlation_matrix[0, 1] ** 2
    
    print(f"\nComplexity Validation Results:")
    print(f"R² correlation with O(n log n): {r_squared:.4f}")
    print(f"Validates theoretical complexity: {'YES' if r_squared > 0.9 else 'NO'}")
    
    return results, r_squared


def demonstrate_algorithm():
    """Demonstrate the algorithm on a realistic scenario."""
    print("VM Reservation Scheduling - Greedy Algorithm Demonstration")
    print("=" * 60)
    
    # Create realistic scenario
    reservations = create_realistic_scenario()
    print(f"Generated {len(reservations)} VM reservations for a business day")
    
    # Solve using greedy algorithm
    selected, rejected = solve_vm_scheduling(reservations)
    
    print(f"\nGreedy Algorithm Results:")
    print(f"Selected: {len(selected)} reservations")
    print(f"Rejected: {len(rejected)} reservations")
    print(f"Success Rate: {len(selected)/len(reservations):.1%}")
    
    # Show selected reservations
    print(f"\nSelected Reservations:")
    for res in selected:
        start_str = res.start_time.strftime("%H:%M")
        end_str = res.end_time.strftime("%H:%M")
        print(f"  {res.id:<20} {start_str}-{end_str}")
    
    # Verify non-overlapping constraint
    overlaps = 0
    for i in range(len(selected)):
        for j in range(i + 1, len(selected)):
            if selected[i].overlaps_with(selected[j]):
                overlaps += 1
    
    print(f"\nVerification:")
    print(f"Overlaps in solution: {overlaps}")
    print(f"Non-overlapping constraint satisfied: {overlaps == 0}")
    
    return selected, rejected


if __name__ == "__main__":
    # Demonstrate the algorithm
    demonstrate_algorithm()
    
    print(f"\n" + "=" * 60)
    
    # Validate complexity
    validate_complexity()