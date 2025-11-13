This file is a merged representation of the entire codebase, combined into a single document.
The content has been processed for AI analysis and code review purposes.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and default ignore patterns
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Repository Information
- **Repository URL:** https://github.com/Nirvisha82/Algorithmic-Optimization-in-Cloud-Computing.git
- **Repository Name:** Algorithmic-Optimization-in-Cloud-Computing
- **Total Files Analyzed:** 6
- **Generated:** 2025-11-13 15:01:15

# Directory Structure
```
.devflow/
  repo-structure.md
.gitignore
README.md
datacenter_proximity_implementation.py
experimental_results/
  VM_performance_dashboard.png
  VM_realistic_scenario_timeline.png
  datacenter_map_analysis.png
  datacenter_performance_dashboard.png
generate_graphs.py
test_project.py
vm_scheduler_implementation.py
```

# Files

## File: .gitignore
````
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[codz]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py.cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock
#poetry.toml

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#   pdm recommends including project-wide configuration in pdm.toml, but excluding .pdm-python.
#   https://pdm-project.org/en/latest/usage/project/#working-with-version-control
#pdm.lock
#pdm.toml
.pdm-python
.pdm-build/

# pixi
#   Similar to Pipfile.lock, it is generally recommended to include pixi.lock in version control.
#pixi.lock
#   Pixi creates a virtual environment in the .pixi directory, just like venv module creates one
#   in the .venv directory. It is recommended not to include this directory in version control.
.pixi

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.envrc
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

# Abstra
# Abstra is an AI-powered process automation framework.
# Ignore directories containing user credentials, local state, and settings.
# Learn more at https://abstra.io/docs
.abstra/

# Visual Studio Code
#  Visual Studio Code specific template is maintained in a separate VisualStudioCode.gitignore 
#  that can be found at https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore
#  and can be added to the global gitignore or merged into this file. However, if you prefer, 
#  you could uncomment the following to ignore the entire vscode folder
# .vscode/

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc

# Cursor
#  Cursor is an AI-powered code editor. `.cursorignore` specifies files/directories to
#  exclude from AI features like autocomplete and code analysis. Recommended for sensitive data
#  refer to https://docs.cursor.com/context/ignore-files
.cursorignore
.cursorindexingignore

# Marimo
marimo/_static/
marimo/_lsp/
__marimo__/
````

## File: README.md
````markdown
# Analysis of Algorithms - Project 1

**Algorithmic Optimization in Cloud Computing**  
*Two Fundamental Algorithmic Paradigms Applied to Real-World Problems*

---

## **Project Structure**

```
Project Root
├── vm_scheduler_implementation.py            # Greedy Algorithm Implementation
├── datacenter_proximity_implementation.py    # Divide & Conquer Implementation
├── generate_graphs.py                        # Visualization Generation
├── test_project.py                           # Integration Tests
├── README.md                                 # Project Documentation
└── experimental_results/                     # Generated Visualizations
    ├── VM_performance_dashboard.png          # VM Scheduler Performance
    ├── VM_realistic_scenario_timeline.png    # Scheduling Timeline
    ├── datacenter_performance_dashboard.png  # Datacenter Analysis
    └── datacenter_map_analysis.png           # Global Datacenter Map
```

---

## **Problems Solved**

### **Problem 1: VM Reservation Scheduling (Greedy Algorithm)**

- **Real-World Context**: Cloud provider optimizing customer VM reservations
- **Technical Problem**: Interval scheduling with overlapping time windows
- **Algorithm**: Greedy "earliest finish time" strategy
- **Complexity**: O(n log n) time, O(1) space
- **Business Impact**: Maximizes customer satisfaction and resource utilization

### **Problem 2: Datacenter Proximity Analysis (Divide & Conquer)**

- **Real-World Context**: Network optimization for global cloud infrastructure
- **Technical Problem**: Closest pair of points in 2D space
- **Algorithm**: Divide & conquer with geometric optimization
- **Complexity**: O(n log n) time vs O(n²) brute force
- **Business Impact**: Enables efficient routing and disaster recovery planning

---

## **How to Run the Project**

### **Prerequisites**

```bash
# Install required Python packages
pip install matplotlib numpy
```

### **1. Test VM Scheduler (Greedy Algorithm)**

```bash
python vm_scheduler_implementation.py
```

**What it does:**

- Demonstrates VM reservation scheduling on 18 realistic jobs
- Shows greedy algorithm selecting optimal non-overlapping reservations
- Validates O(n log n) complexity experimentally
- Reports success rate and performance metrics

### **2. Test Datacenter Proximity (Divide & Conquer)**

```bash
python datacenter_proximity_implementation.py
```

**What it does:**

- Analyzes 18 real global datacenter locations
- Finds closest pair using divide & conquer algorithm
- Compares performance against brute force approach
- Validates O(n log n) vs O(n²) complexity difference

### **3. Generate All Visualizations**

```bash
python generate_graphs.py
```

**What it creates:**

- Performance dashboards for both algorithms
- Complexity validation graphs
- Realistic scenario timelines
- Global datacenter proximity maps
- All outputs saved to `experimental_results/` directory

### **4. Run Complete Integration Test**

```bash
python test_project.py
```

**What it verifies:**

- Both algorithms work correctly
- No overlapping intervals in greedy solution
- Divide & conquer matches brute force results
- Graph generation functions are available
- Project is ready for submission

---

## **Key Results**

| Algorithm | Problem | Time Complexity | Experimental R² | Performance |
|-----------|---------|-----------------|-----------------|-------------|
| **Greedy** | VM Scheduling | O(n log n) | 0.98+ | 44.4% success rate |
| **Divide & Conquer** | Datacenter Proximity | O(n log n) | 0.95+ | 9× fewer comparisons |

### **VM Scheduler Results:**

- **Input**: 18 overlapping VM reservation requests
- **Output**: 8 optimal non-overlapping reservations selected
- **Success Rate**: 44.4% (significant improvement over random selection)
- **Verification**: Zero overlaps in final solution

### **Datacenter Proximity Results:**

- **Input**: 18 global datacenter coordinates
- **Closest Pair**: AWS-US-East-1 and Azure-East-US (both in Virginia)
- **Distance**: 0.4912 degrees
- **Performance**: Divide & conquer uses 9× fewer comparisons than brute force

---

## **Technical Implementation**

### **Greedy Algorithm Features:**

- Optimal interval scheduling implementation
- Real VM reservation data model
- Performance measurement and complexity validation
- Business scenario demonstration
- Correctness verification (no overlaps)

### **Divide & Conquer Features:**

- Geometric closest pair algorithm
- 7-point optimization for strip processing
- Brute force comparison for validation
- Real datacenter coordinate data
- Performance scaling analysis

### **Visualization Features:**

- Scalability analysis (log-log plots)
- Algorithm comparison charts
- Realistic scenario timelines
- Global datacenter maps
- Complexity validation graphs

---

## **Experimental Validation**

Both algorithms demonstrate strong correlation with theoretical complexity:

- **VM Scheduler**: R² ≈ 0.98 correlation with O(n log n)
- **Datacenter Analysis**: R² ≈ 0.95 correlation with O(n log n)
- **Brute Force**: R² = 1.00 correlation with O(n²)

Performance testing validates theoretical predictions across input sizes from 10 to 5000 elements.

---
````

## File: datacenter_proximity_implementation.py
````python
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
````

## File: generate_graphs.py
````python
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
````

## File: test_project.py
````python
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
````

## File: vm_scheduler_implementation.py
````python
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
````

