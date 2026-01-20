import numpy as np

# Read the output data
try:
    with open('/tmp/circuit_data.txt', 'r') as f:
        lines = f.readlines()
    
    # Parse the data
    data = []
    for line in lines[1:]:  # Skip header
        line = line.strip()
        if not line:
            continue
        
        parts = line.split()
        if len(parts) >= 3:
            try:
                idx = float(parts[0])
                vg = float(parts[1])
                vd = float(parts[2])
                data.append((vg, vd))
            except ValueError:
                continue
    
    if data:
        vg_vals = np.array([d[0] for d in data])
        vd_vals = np.array([d[1] for d in data])
        
        # Calculate derivative dv(d)/dv(g)
        slopes = np.diff(vd_vals) / np.diff(vg_vals)
        slope_vg = vg_vals[:-1] + np.diff(vg_vals) / 2
        
        print("\n" + "="*70)
        print("NOISE MARGIN ANALYSIS - Finding points where slope = -1")
        print("="*70)
        
        # For noise margin calculation, we need to find where the transfer curve
        # intersects with the line y = x (unity gain line). At these points, slope = -1
        # means dv(d) = -dv(g), which is equivalent to the point where the gain = -1
        
        # We're looking for two intersections with slope = -1
        differences = slopes - (-1.0)
        
        print("\nFull slope analysis around slope = -1:\n")
        print("Index\tv(g) [V]\t v(d) [V]\t slope\t\tError from -1")
        print("-"*75)
        for i, (vg, vd, slope) in enumerate(zip(slope_vg, slopes, slopes)):
            error = abs(slope - (-1.0))
            if error < 1.0:  # Print slopes relatively close to -1
                print(f"{i}\t{vg:.6f}\t {(vd_vals[i] + vd_vals[i+1])/2:.6f}\t {slope:.6f}\t {error:.6f}")
        
        # Find where slope is approximately -1
        tolerance = 0.20
        close_indices = np.where(np.abs(differences) < tolerance)[0]
        
        if len(close_indices) > 0:
            print(f"\n{'='*70}")
            print(f"Points where slope ≈ -1 (within ±{tolerance}):")
            print(f"{'='*70}\n")
            
            for idx in close_indices:
                vg_at_slope = slope_vg[idx]
                vd_at_slope = (vd_vals[idx] + vd_vals[idx+1]) / 2
                actual_slope = slopes[idx]
                print(f"  x = {vg_at_slope:.6f} V, y = {vd_at_slope:.6f} V, slope = {actual_slope:.6f}")
            
            # For noise margin, we need to use the appropriate points
            # The two x values where slope ≈ -1 are the transition points
            if len(close_indices) >= 2:
                print(f"\n{'='*70}")
                print("SOLUTION: Two x values where slope = -1")
                print(f"{'='*70}\n")
                /tmp/circuit_data.txt
                idx1 = close_indices[0]
                idx2 = close_indices[-1]
                
                x1 = slope_vg[idx1]
                y1 = (vd_vals[idx1] + vd_vals[idx1+1]) / 2
                
                x2 = slope_vg[idx2]
                y2 = (vd_vals[idx2] + vd_vals[idx2+1]) / 2
                
                print(f"First x value: {x1:.6f} V")
                print(f"Corresponding y value: {y1:.6f} V\n")
                
                print(f"Second x value: {x2:.6f} V")
                print(f"Corresponding y value: {y2:.6f} V\n")
        else:
            print(f"\nNo points found with slope within ±{tolerance} of -1")
        
    else:
        print("No data extracted from simulation output")
        
except FileNotFoundError:
    print("Data file not found at /tmp/circuit_data.txt")
    print("Run extract_data.cir first:")
    print("  cd /home/student/Documents/U24EC123/DIC_LAB3")
    print("  ngspice -b extract_data.cir")
except Exception as e:
    print(f"Error processing data: {e}")
