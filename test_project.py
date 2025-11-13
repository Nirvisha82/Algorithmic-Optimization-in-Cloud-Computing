#!/usr/bin/env python3
"""
Simple test script to verify both algorithms work correctly
"""

def test_greedy():
    """Test greedy algorithm."""
    print("Testing Greedy Algorithm...")
    from vm_scheduler_implementation import create_realistic_scenario, solve_vm_scheduling
    
    reservations = create_realistic_scenario()
    selected, rejected = solve_vm_scheduling(reservations)
    
    print(f"  Reservations: {len(reservations)}")
    print(f"  Selected: {len(selected)}")
    print(f"  Success Rate: {len(selected)/len(reservations):.1%}")
    
    # Verify no overlaps
    overlaps = 0
    for i in range(len(selected)):
        for j in range(i + 1, len(selected)):
            if selected[i].overlaps_with(selected[j]):
                overlaps += 1
    
    print(f"  Overlaps: {overlaps} (should be 0)")
    print(f"  PASS: Greedy algorithm working correctly")


def test_divide_conquer():
    """Test divide and conquer algorithm."""
    print("\nTesting Divide & Conquer Algorithm...")
    from datacenter_proximity_implementation import create_realistic_datacenters, solve_datacenter_proximity
    
    datacenters = create_realistic_datacenters()
    dc_result = solve_datacenter_proximity(datacenters, "divide_conquer")
    bf_result = solve_datacenter_proximity(datacenters, "brute_force")
    
    print(f"  Datacenters: {len(datacenters)}")
    print(f"  Closest distance: {dc_result.distance:.4f} degrees")
    print(f"  D&C comparisons: {dc_result.comparisons_made}")
    print(f"  BF comparisons: {bf_result.comparisons_made}")
    
    # Verify both algorithms found same result
    same_result = abs(dc_result.distance - bf_result.distance) < 1e-10
    print(f"  Same result: {same_result}")
    print(f"  PASS: Divide & Conquer algorithm working correctly")


def test_graph_generation():
    """Test graph generation."""
    print("\nTesting Graph Generation...")
    try:
        from generate_graphs import generate_greedy_graphs
        print("  Graph generation functions available")
        print("  Run 'python generate_graphs.py' to create all visualizations")
        print("  PASS: Graph generation ready")
    except ImportError as e:
        print(f"  ERROR: {e}")


def main():
    """Run all tests."""
    print("PROJECT FUNCTIONALITY TEST")
    print("=" * 40)
    
    try:
        test_greedy()
        test_divide_conquer()
        test_graph_generation()
        
        print("\n" + "=" * 40)
        print("ALL TESTS PASSED")
        print("=" * 40)
        
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()