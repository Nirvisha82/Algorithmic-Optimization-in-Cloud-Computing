#!/usr/bin/env python3
"""
Datacenter Proximity Finder - Divide and Conquer Implementation
Closest Pair of Points Problem for Geographic Data Center Analysis
"""

import math
import time
import random
from typing import List, Tuple
from dataclasses import dataclass
import numpy as np


@dataclass
class DataCenter:
    """Represents a data center with GPS coordinates."""   
    id: str
    name: str
    latitude: float   # GPS latitude in decimal degrees
    longitude: float  # GPS longitude in decimal degrees
    
    def to_point(self) -> Tuple[float, float]:
        return (self.longitude, self.latitude)
    
    def distance_to(self, other: 'DataCenter') -> float:
        return euclidean_distance(self.to_point(), other.to_point())
    
    def __str__(self) -> str:
        return f"{self.name} ({self.latitude:.4f}, {self.longitude:.4f})"


@dataclass
class ClosestPairResult:
    """Result of closest pair algorithm."""
    point1: Tuple[float, float]
    point2: Tuple[float, float]
    distance: float
    algorithm_used: str
    execution_time: float
    comparisons_made: int


def euclidean_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def brute_force_closest_pair(points: List[Tuple[float, float]]) -> Tuple[Tuple[float, float], Tuple[float, float], float, int]:
    """Brute force algorithm for closest pair of points."""
    if len(points) < 2:
        raise ValueError("Need at least 2 points")
    
    min_distance = float('inf')
    closest_pair = (points[0], points[1])
    comparisons = 0
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            comparisons += 1
            
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    
    return closest_pair[0], closest_pair[1], min_distance, comparisons


def closest_pair_divide_conquer(points: List[Tuple[float, float]]) -> Tuple[Tuple[float, float], Tuple[float, float], float, int]:
    """Divide and conquer algorithm for closest pair of points."""
    if len(points) < 2:
        raise ValueError("Need at least 2 points")
    
    # Sort points by x-coordinate for divide step
    points_x = sorted(points, key=lambda p: p[0])
    # Sort points by y-coordinate for strip processing
    points_y = sorted(points, key=lambda p: p[1])
    
    # Call recursive function
    result = _closest_pair_rec(points_x, points_y)
    return result[0], result[1], result[2], result[3]


def _closest_pair_rec(px: List[Tuple[float, float]], py: List[Tuple[float, float]]) -> Tuple[Tuple[float, float], Tuple[float, float], float, int]:
    """Recursive helper function for divide and conquer closest pair."""
    n = len(px)
    
    # Base case: use brute force for small instances
    if n <= 3:
        return brute_force_closest_pair(px)
    
    # Divide: find the middle point
    mid = n // 2
    midpoint = px[mid]
    
    # Split points into left and right halves
    pyl = [point for point in py if point[0] < midpoint[0] or (point[0] == midpoint[0] and point[1] < midpoint[1])]
    pyr = [point for point in py if point not in pyl]
    
    # Conquer: recursively solve left and right halves
    left_result = _closest_pair_rec(px[:mid], pyl)
    right_result = _closest_pair_rec(px[mid:], pyr)
    
    # Find minimum distance from both halves
    if left_result[2] <= right_result[2]:
        min_distance = left_result[2]
        closest_pair = (left_result[0], left_result[1])
        total_comparisons = left_result[3] + right_result[3]
    else:
        min_distance = right_result[2]
        closest_pair = (right_result[0], right_result[1])
        total_comparisons = left_result[3] + right_result[3]
    
    # Combine: check points in the strip around the dividing line
    strip_result = _find_closest_in_strip(py, midpoint[0], min_distance)
    
    total_comparisons += strip_result[3]
    
    # Return the overall closest pair
    if strip_result[2] < min_distance:
        return strip_result[0], strip_result[1], strip_result[2], total_comparisons
    else:
        return closest_pair[0], closest_pair[1], min_distance, total_comparisons


def _find_closest_in_strip(py: List[Tuple[float, float]], center_x: float, delta: float) -> Tuple[Tuple[float, float], Tuple[float, float], float, int]:
    """Find closest pair in the strip around the dividing line."""
    # Create strip of points within delta of the center line
    strip = [point for point in py if abs(point[0] - center_x) < delta]
    
    min_distance = delta
    closest_pair = (None, None)
    comparisons = 0
    
    # Check each point against at most 7 points ahead
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_distance:
            distance = euclidean_distance(strip[i], strip[j])
            comparisons += 1
            
            if distance < min_distance:
                min_distance = distance
                closest_pair = (strip[i], strip[j])
            
            j += 1
            if j - i > 7:
                break
    
    if closest_pair[0] is None:
        return py[0], py[1], delta, comparisons  # No closer pair found
    else:
        return closest_pair[0], closest_pair[1], min_distance, comparisons


def create_realistic_datacenters() -> List[DataCenter]:
    """Create a realistic set of data centers with GPS coordinates."""
    
    # Real-world major data center locations (approximate coordinates)
    datacenter_specs = [
        ("AWS-US-East-1", "Virginia", 39.0458, -77.5081),
        ("AWS-US-West-2", "Oregon", 45.5152, -122.6784),
        ("AWS-EU-West-1", "Ireland", 53.3498, -6.2603),
        ("GCP-US-Central1", "Iowa", 41.5868, -93.6250),
        ("Azure-East-US", "Virginia", 38.9072, -77.0369),
        ("Azure-West-Europe", "Netherlands", 52.3676, 4.9041),
        ("AWS-AP-Southeast-1", "Singapore", 1.3521, 103.8198),
        ("GCP-Europe-West1", "Belgium", 50.8503, 4.3517),
        ("Azure-Japan-East", "Tokyo", 35.6762, 139.6503),
        ("AWS-SA-East-1", "São Paulo", -23.5505, -46.6333),
        ("GCP-US-East1", "South Carolina", 32.7767, -80.7436),
        ("Azure-Australia-East", "Sydney", -33.8688, 151.2093),
        ("AWS-CA-Central-1", "Canada", 45.4215, -75.6972),
        ("GCP-Asia-East1", "Taiwan", 25.0330, 121.5654),
        ("Azure-UK-South", "London", 51.5074, -0.1278),
        ("AWS-EU-Central-1", "Frankfurt", 50.1109, 8.6821),
        ("GCP-US-West1", "California", 37.7749, -122.4194),
        ("Azure-Central-India", "Pune", 18.5204, 73.8567),
    ]
    
    datacenters = []
    for i, (name, location, lat, lon) in enumerate(datacenter_specs):
        datacenter = DataCenter(
            id=f"dc-{i+1:02d}",
            name=f"{name}-{location}",
            latitude=lat,
            longitude=lon
        )
        datacenters.append(datacenter)
    
    return datacenters


def solve_datacenter_proximity(datacenters: List[DataCenter], algorithm: str = "divide_conquer") -> ClosestPairResult:
    """Solve the datacenter proximity problem using specified algorithm."""
    # Convert datacenters to points
    points = [dc.to_point() for dc in datacenters]
    
    # Measure execution time
    start_time = time.perf_counter()
    
    if algorithm == "brute_force":
        p1, p2, distance, comparisons = brute_force_closest_pair(points)
    elif algorithm == "divide_conquer":
        p1, p2, distance, comparisons = closest_pair_divide_conquer(points)
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    return ClosestPairResult(
        point1=p1,
        point2=p2,
        distance=distance,
        algorithm_used=algorithm,
        execution_time=execution_time,
        comparisons_made=comparisons
    )


def measure_algorithm_performance(sizes: List[int], num_trials: int = 3) -> Tuple[List[Tuple[int, float]], List[Tuple[int, float]]]:
    """Measure performance of both algorithms for complexity validation."""
    dc_results = []
    bf_results = []
    
    for n in sizes:
        dc_times = []
        bf_times = []
        
        for _ in range(num_trials):
            # Generate random points
            points = [(random.uniform(-180, 180), random.uniform(-90, 90)) for _ in range(n)]
            
            # Measure divide and conquer
            start_time = time.perf_counter()
            closest_pair_divide_conquer(points)
            end_time = time.perf_counter()
            dc_times.append(end_time - start_time)
            
            # Measure brute force (only for smaller sizes to avoid long waits)
            if n <= 1000:
                start_time = time.perf_counter()
                brute_force_closest_pair(points)
                end_time = time.perf_counter()
                bf_times.append(end_time - start_time)
        
        dc_avg = sum(dc_times) / len(dc_times)
        dc_results.append((n, dc_avg))
        print(f"Size {n:4d}: Divide&Conquer = {dc_avg:.6f}s", end="")
        
        if bf_times:
            bf_avg = sum(bf_times) / len(bf_times)
            bf_results.append((n, bf_avg))
            print(f", Brute Force = {bf_avg:.6f}s")
        else:
            print()
    
    return dc_results, bf_results


def validate_complexity():
    """Validate O(n log n) vs O(n²) complexity experimentally."""
    print("Validating Divide and Conquer O(n log n) vs Brute Force O(n²) complexity...")
    
    sizes = [10, 50, 100, 500, 1000, 2000, 5000]
    dc_results, bf_results = measure_algorithm_performance(sizes)
    
    # Calculate theoretical complexity correlations
    dc_sizes = np.array([r[0] for r in dc_results])
    dc_times = np.array([r[1] for r in dc_results])
    
    # Theoretical O(n log n) curve
    theoretical_nlogn = dc_sizes * np.log2(dc_sizes)
    correlation_nlogn = np.corrcoef(theoretical_nlogn, dc_times)[0, 1] ** 2
    
    print(f"\nDivide and Conquer Complexity Validation:")
    print(f"R² correlation with O(n log n): {correlation_nlogn:.4f}")
    print(f"Validates O(n log n) complexity: {'YES' if correlation_nlogn > 0.9 else 'NO'}")
    
    if bf_results:
        bf_sizes = np.array([r[0] for r in bf_results])
        bf_times = np.array([r[1] for r in bf_results])
        
        # Theoretical O(n²) curve
        theoretical_n2 = bf_sizes ** 2
        correlation_n2 = np.corrcoef(theoretical_n2, bf_times)[0, 1] ** 2
        
        print(f"\nBrute Force Complexity Validation:")
        print(f"R² correlation with O(n²): {correlation_n2:.4f}")
        print(f"Validates O(n²) complexity: {'YES' if correlation_n2 > 0.9 else 'NO'}")
    
    return dc_results, bf_results


def demonstrate_algorithm():
    """Demonstrate the algorithm on realistic datacenter scenario."""
    print("Datacenter Proximity Finder - Divide and Conquer Demonstration")
    print("=" * 70)
    
    # Create realistic datacenters
    datacenters = create_realistic_datacenters()
    print(f"Analyzing {len(datacenters)} major cloud data centers worldwide")
    
    # Solve using both algorithms
    dc_result = solve_datacenter_proximity(datacenters, "divide_conquer")
    bf_result = solve_datacenter_proximity(datacenters, "brute_force")
    
    print(f"\nResults:")
    print(f"Closest pair distance: {dc_result.distance:.4f} degrees")
    print(f"Point 1: ({dc_result.point1[0]:.4f}, {dc_result.point1[1]:.4f})")
    print(f"Point 2: ({dc_result.point2[0]:.4f}, {dc_result.point2[1]:.4f})")
    
    # Find which datacenters these correspond to
    for dc in datacenters:
        point = dc.to_point()
        if (abs(point[0] - dc_result.point1[0]) < 0.0001 and abs(point[1] - dc_result.point1[1]) < 0.0001):
            print(f"Datacenter 1: {dc}")
        elif (abs(point[0] - dc_result.point2[0]) < 0.0001 and abs(point[1] - dc_result.point2[1]) < 0.0001):
            print(f"Datacenter 2: {dc}")
    
    print(f"\nPerformance Comparison:")
    print(f"Divide & Conquer: {dc_result.execution_time:.6f}s, {dc_result.comparisons_made} comparisons")
    print(f"Brute Force:      {bf_result.execution_time:.6f}s, {bf_result.comparisons_made} comparisons")
    print(f"Speedup: {bf_result.execution_time / dc_result.execution_time:.2f}x")
    print(f"Comparison reduction: {bf_result.comparisons_made / dc_result.comparisons_made:.2f}x fewer")
    
    # Verify both algorithms found the same result
    same_distance = abs(dc_result.distance - bf_result.distance) < 1e-10
    print(f"\nVerification:")
    print(f"Both algorithms found same result: {'YES' if same_distance else 'NO'}")
    
    return dc_result, bf_result


if __name__ == "__main__":
    # Demonstrate the algorithm
    demonstrate_algorithm()
    
    print(f"\n" + "=" * 70)
    
    # Validate complexity
    validate_complexity()
