# NMOS Inverter Slope Analysis Results

## Question: Find x and y where the slope of v(d) vs v(g) equals -1

### Answer:

**x (v(g)) = 0.025000 V**
**y (v(d)) = 1.153642 V**
**Actual slope at this point = -0.955600**

This is the closest point to slope = -1 in the transfer characteristic curve.

---

## Analysis Details:

### Circuit Configuration:
- NMOS transistor (W = 32μm, L = 65nm)
- VDD = 1.2V
- Load resistor = 10kΩ
- DC sweep: vin from 0V to 1.2V in 0.01V steps
- Total data points: 121

### Key Observations:
1. The slope reaches its minimum (steepest) around v(g) ≈ 0.2V
2. At v(g) = 0.025V, the slope is -0.956 (very close to -1)
3. As input voltage increases beyond 0.2V, the slope becomes less steep
4. By v(g) ≈ 0.35V, the circuit enters the saturation region

### Significance:
The transfer characteristic slope of approximately -1 occurs in the early transition region of the inverter. This represents the point where the output voltage is beginning to change significantly with input voltage changes.

The steepest slope (-5.18) occurs around v(g) ≈ 0.22V, which is the maximum gain region of the inverter.
