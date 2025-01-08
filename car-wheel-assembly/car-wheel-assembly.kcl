// Car Wheel Assembly
// A car wheel assembly with a rotor, tire, and lug nuts.


// Car Wheel
// A sports car wheel with a circular lug pattern and spokes.


// Define constants
lugCount = 5
lugSpacing = 114.3
offset = -35
backSpacing = 6.38
wheelWidth = 9.5
wheelDiameter = 19

// Create the circular pattern for the lug holes
circles = startSketchOn('XZ')
  |> circle({
       center = [lugSpacing / 2, 0],
       radius = 16 / 2
     }, %)
  |> patternCircular2d({
       arcDegrees = 360,
       center = [0, 0],
       instances = lugCount,
       rotateDuplicates = true
     }, %)

// Create the wheel center and add lug holes
flangeBase = startSketchOn('XZ')
  |> circle({
       center = [0, 0],
       radius = lugSpacing / 2 + 16 + 5
     }, %)
  |> hole(circles, %)
  |> extrude(10, %)

// Remove the interior of the wheel center
sketch001 = startSketchOn(flangeBase, 'END')
  |> circle({ center = [0, 0], radius = 20 }, %)
  |> extrude(-10, %)

// Add more material to the wheel center
sketch002 = startSketchOn(flangeBase, 'END')
  |> circle({
       center = [0, 0],
       radius = lugSpacing / 2 + 16 + 8
     }, %)
  |> extrude(30, %)

// Edge treatment around center
sketch003 = startSketchOn('XY')
  |> startProfileAt([lugSpacing / 2 + 16 + 8, -10 - 30], %)
  |> yLine(30, %)
  |> line([6, -2], %)
  |> lineTo([profileStartX(%), profileStartY(%)], %)
  |> close(%)
  |> revolve({ axis = 'y' }, %)

// Center cap
sketch004 = startSketchOn('XY')
  |> startProfileAt([15, -40], %)
  |> xLine(15, %)
  |> line([-3.01, -3.54], %)
  |> line([-8.8, 0.17], %)
  |> lineTo([profileStartX(%), profileStartY(%)], %)
  |> close(%)
  |> revolve({ axis = 'y' }, %)

// Holes for lug nut heads
sketch005 = startSketchOn(sketch002, 'END')
  |> circle({
       center = [lugSpacing / 2, 0],
       radius = 17
     }, %)
  |> patternCircular2d({
       arcDegrees = 360,
       center = [0, 0],
       instances = lugCount,
       rotateDuplicates = true
     }, %)

sketch006 = extrude(-30, sketch005)

// Seperating the spoke base planes
plane001 = {
  plane = {
    origin = [0.0, 0.0, 5.0],
    xAxis = [1.0, 0.0, 0.0],
    yAxis = [0.0, 1.0, 0.0],
    zAxis = [0.0, 0.0, 1.0]
  }
}

plane002 = {
  plane = {
    origin = [0.0, 0.0, -5.0],
    xAxis = [1.0, 0.0, 0.0],
    yAxis = [0.0, 1.0, 0.0],
    zAxis = [0.0, 0.0, 1.0]
  }
}

// Spoke cross sections
sketch007 = startSketchOn(plane001)
  |> startProfileAt([lugSpacing / 2 + 17, -36], %)
  |> bezierCurve({
       to = [
         wheelDiameter * 25.4 / 2 - (lugSpacing / 2) - 35,
         12
       ],
       control1 = [
         (wheelDiameter * 25.4 / 2 - (lugSpacing / 2) - 35) / 2,
         0
       ],
       control2 = [
         (wheelDiameter * 25.4 / 2 - (lugSpacing / 2) - 35) / 2,
         15
       ]
     }, %)
  |> yLine(12, %)
  |> bezierCurve({
       to = [
         -wheelDiameter * 25.4 / 2 + lugSpacing / 2 + 35,
         -12
       ],
       control1 = [
         -(wheelDiameter * 25.4 / 2 - (lugSpacing / 2) - 16) / 2,
         0
       ],
       control2 = [
         -(wheelDiameter * 25.4 / 2 - (lugSpacing / 2) - 16) / 2,
         -15
       ]
     }, %)
  |> close(%)

sketch008 = startSketchOn(plane002)
  |> startProfileAt([lugSpacing / 2 + 17, -36], %)
  |> bezierCurve({
       to = [
         wheelDiameter * 25.4 / 2 - (lugSpacing / 2) - 35,
         12
       ],
       control1 = [
         (wheelDiameter * 25.4 / 2 - (lugSpacing / 2) - 35) / 2,
         0
       ],
       control2 = [
         (wheelDiameter * 25.4 / 2 - (lugSpacing / 2) - 35) / 2,
         15
       ]
     }, %)
  |> yLine(12, %)
  |> bezierCurve({
       to = [
         -wheelDiameter * 25.4 / 2 + lugSpacing / 2 + 35,
         -12
       ],
       control1 = [
         -(wheelDiameter * 25.4 / 2 - (lugSpacing / 2) - 16) / 2,
         0
       ],
       control2 = [
         -(wheelDiameter * 25.4 / 2 - (lugSpacing / 2) - 16) / 2,
         -15
       ]
     }, %)
  |> close(%)

// Circular pattern spokes
sketch009 = extrude(20, sketch007)
  |> patternCircular3d({
       axis = [0, 1, 0],
       center = [0, -2000, 0],
       instances = 6,
       arcDegrees = 360,
       rotateDuplicates = true
     }, %)

sketch0010 = extrude(-20, sketch008)
  |> patternCircular3d({
       axis = [0, 1, 0],
       center = [0, -2000, 0],
       instances = 6,
       arcDegrees = 360,
       rotateDuplicates = true
     }, %)

// Wheel exterior
sketch0011 = startSketchOn('XY')
  |> startProfileAt([
       wheelDiameter * 25.4 / 2,
       -wheelWidth * 25.4 + backSpacing * 25.4 + offset
     ], %)
  |> line([wheelWidth * 2, -wheelWidth], %)
  |> yLine(-wheelWidth * 2, %)
  |> xLine(-wheelWidth, %)
  |> yLine(wheelWidth * 1.5, %)
  |> line([-wheelWidth * 2, wheelWidth], %)
  |> yLine(wheelWidth * 2.7, %)
  |> line([-wheelWidth, wheelWidth], %)
  |> yLine(wheelWidth * 9, %)
  |> line([wheelWidth, wheelWidth], %)
  |> yLine(wheelWidth * 11, %)
  |> line([wheelWidth * 2, wheelWidth], %)
  |> yLine(wheelWidth * 2, %)
  |> xLine(wheelWidth, %)
  |> yLine(-wheelWidth * 2.7, %)
  |> line([-wheelWidth * 2, -wheelWidth], %)
  |> yLine(-wheelWidth * 11, %)
  |> line([-wheelWidth, -wheelWidth], %)
  |> yLine(-wheelWidth * 7.7, %)
  |> line([wheelWidth, -wheelWidth], %)
  |> lineTo([profileStartX(%), profileStartY(%)], %)
  |> close(%)
  |> revolve({ axis = 'y' }, %)

rotorDiameter = 12
rotorInnerDiameter = 6
rotorSinglePlateThickness = 6.3
rotorInnerDiameterThickness = 12.6
lugHolePatternDia = 3
yAxisOffset = 10
rotorTotalThickness = 25.4
spacerPatternDiameter = 11
spacerDiameter = 6.3
spacerLength = rotorTotalThickness - (2 * rotorSinglePlateThickness)
spacerCount = 16
wheeldiameter = 19

rotorPlane = {
  plane = {
    origin = { x = 0, y = yAxisOffset, z = 0 },
    xAxis = { x = -1, y = 0, z = 0 },
    yAxis = { x = 0, y = 0, z = 1 },
    zAxis = { x = 0, y = 1, z = 0 }
  }
}

fn lugPattern(plane) {
  lugHolePattern = circle({
         center = [-lugSpacing / 2, 0],
         radius = 8
       }, plane)
    |> patternCircular2d({
         arcDegrees = 360,
         center = [0, 0],
         instances = lugCount,
         rotateDuplicates = true
       }, %)
  return lugHolePattern
}

rotorSketch = startSketchOn(rotorPlane)
  |> circle({
       center = [0, 0],
       radius = rotorDiameter / 2 * 25.4
     }, %)
  |> hole(lugPattern(%), %)
rotor = extrude(rotorSinglePlateThickness, rotorSketch)

rotorBumpSketch = startSketchOn(rotorPlane)
  |> circle({
       center = [0, 0],
       radius = rotorInnerDiameter / 2 * 25.4
     }, %)
  |> hole(lugPattern(%), %)
rotorBump = extrude(-rotorInnerDiameterThickness, rotorBumpSketch)

rotorSecondaryPlatePlane = {
  plane = {
    origin = {
      x = 0,
      y = 10 + rotorTotalThickness * 0.75,
      z = 0
    },
    xAxis = { x = -1, y = 0, z = 0 },
    yAxis = { x = 0, y = 0, z = 1 },
    zAxis = { x = 0, y = 1, z = 0 }
  }
}

secondaryRotorSketch = startSketchOn(rotorSecondaryPlatePlane)
  |> circle({
       center = [0, 0],
       radius = rotorDiameter / 2 * 25.4
     }, %)
  |> hole(lugPattern(%), %)

secondRotor = extrude(rotorSinglePlateThickness, secondaryRotorSketch)

spacerSketch = startSketchOn(rotorSecondaryPlatePlane)
  |> circle({
       center = [spacerPatternDiameter / 2 * 25.4, 0],
       radius = spacerDiameter
     }, %)
  |> patternCircular2d({
       arcDegrees = 360,
       center = [0, 0],
       instances = spacerCount + 1,
       rotateDuplicates = true
     }, %)

spacers = extrude(-spacerLength, spacerSketch)

// Lug Nut
// lug Nuts are essential components used to create secure connections, whether for electrical purposes, like terminating wires or grounding, or for mechanical purposes, such as providing mounting points or reinforcing structural joints.


// Define constants
lugDiameter = 24
lugHeadLength = lugDiameter * .5
lugThreadDiameter = lugDiameter / 2 * .85 // mm
lugLength = 30 // mm
lugThreadDepth = lugLength - 12.7 // mm


// Define the plane the lugs live on
customPlane = {
  plane = {
    origin = { x = lugSpacing / 2, y = -30, z = 0 },
    xAxis = { x = 1, y = 0, z = 0 },
    yAxis = { x = 0, y = -1, z = 0 },
    zAxis = { x = 0, y = 0, z = 1 }
  }
}

// Create a function for the lug nuts
fn lug(plane, length, diameter) {
  lugSketch = startSketchOn(customPlane)
    |> startProfileAt([0 + diameter / 2, 0], %)
    |> angledLineOfYLength({ angle = 70, length = lugHeadLength }, %)
    |> xLineTo(lugDiameter / 2, %)
    |> yLineTo(lugLength, %)
    |> tangentialArc({ offset = 90, radius = 3 }, %)
    |> xLineTo(0 + .001, %, $c1)
    |> yLineTo(lugThreadDepth, %)
    |> xLineTo(lugThreadDiameter, %)
    |> yLineTo(0, %)
    |> close(%)
    |> revolve({ axis = "Y" }, %)
  return lugSketch
}

lug(customPlane, lugLength, lugDiameter)
  |> patternCircular3d({
       arcDegrees = 360,
       axis = [0, 1, 0],
       center = [0, 0, 0],
       instances = lugCount,
       rotateDuplicates = false
     }, %)

  // Tire
  // A tire is a critical component of a vehicle that provides the necessary traction and grip between the car and the road. It supports the vehicle's weight and absorbs shocks from road irregularities.

// Define constants
tireInnerDiameter = 19 * 25.4
tireOuterDiameter = 26 * 25.4
tireDepth = 280
bendRadius = 40
tireTreadWidth = 10
tireTreadDepth = 10
tireTreadOffset = 80

// Create the sketch of the tire
tireSketch = startSketchOn("XY")
  |> startProfileAt([tireInnerDiameter / 2, tireDepth / 2], %)
  |> lineTo([
       tireOuterDiameter / 2 - bendRadius,
       tireDepth / 2
     ], %, $edge1)
  |> tangentialArc({ offset = -90, radius = bendRadius }, %)
  |> lineTo([
       tireOuterDiameter / 2,
       tireDepth / 2 - tireTreadOffset
     ], %)
  |> line([-tireTreadDepth, 0], %)
  |> line([0, -tireTreadWidth], %)
  |> line([tireTreadDepth, 0], %)
  |> lineTo([
       tireOuterDiameter / 2,
       -tireDepth / 2 + tireTreadOffset + tireTreadWidth
     ], %)
  |> line([-tireTreadDepth, 0], %)
  |> line([0, -tireTreadWidth], %)
  |> line([tireTreadDepth, 0], %)
  |> lineTo([
       tireOuterDiameter / 2,
       -tireDepth / 2 + bendRadius
     ], %)
  |> tangentialArc({ offset = -90, radius = bendRadius }, %)
  |> lineTo([tireInnerDiameter / 2, -tireDepth / 2], %, $edge2)
  |> close(%)
tire = revolve({ axis = "Y" }, tireSketch)

// Brake Caliper
// Brake calipers are used to squeeze the brake pads against the rotor, causing larger and larger amounts of friction depending on how hard the brakes are pressed.


// Define constants
caliperTolerance = 5
caliperPadLength = 40
caliperThickness = 10
caliperOuterEdgeRadius = 10
caliperInnerEdgeRadius = 3

// Create the plane for the brake caliper. This is so it can match up with the rotor model.
brakeCaliperPlane = {
  plane = {
    origin = { x = 0, y = 0, z = 0 },
    xAxis = { x = 1, y = 0, z = 0 },
    yAxis = { x = 0, y = 1, z = 0 },
    zAxis = { x = 0, y = 0, z = 1 }
  }
}

// Sketch the brake caliper profile
brakeCaliperSketch = startSketchOn(brakeCaliperPlane)
  |> startProfileAt([
       rotorDiameter / 2 * 25.4 + caliperTolerance,
       0
     ], %)
  |> line([
       0,
       rotorTotalThickness + caliperTolerance - caliperInnerEdgeRadius
     ], %)
  |> tangentialArc({
       offset = 90,
       radius = caliperInnerEdgeRadius
     }, %)
  |> line([
       -caliperPadLength + 2 * caliperInnerEdgeRadius,
       0
     ], %)
  |> tangentialArc({
       offset = -90,
       radius = caliperInnerEdgeRadius
     }, %)
  |> line([
       0,
       caliperThickness - (caliperInnerEdgeRadius * 2)
     ], %)
  |> tangentialArc({
       offset = -90,
       radius = caliperInnerEdgeRadius
     }, %)
  |> line([
       caliperPadLength + caliperThickness - caliperOuterEdgeRadius - caliperInnerEdgeRadius,
       0
     ], %)
  |> tangentialArc({
       offset = -90,
       radius = caliperOuterEdgeRadius
     }, %)
  |> line([
       0,
       -2 * caliperTolerance - (2 * caliperThickness) - rotorTotalThickness + 2 * caliperOuterEdgeRadius
     ], %)
  |> tangentialArc({
       offset = -90,
       radius = caliperOuterEdgeRadius
     }, %)
  |> line([
       -caliperPadLength - caliperThickness + caliperOuterEdgeRadius + caliperInnerEdgeRadius,
       0
     ], %)
  |> tangentialArc({
       offset = -90,
       radius = caliperInnerEdgeRadius
     }, %)
  |> line([
       0,
       caliperThickness - (2 * caliperInnerEdgeRadius)
     ], %)
  |> tangentialArc({
       offset = -90,
       radius = caliperInnerEdgeRadius
     }, %)
  |> line([
       caliperPadLength - (2 * caliperInnerEdgeRadius),
       0
     ], %)
  |> tangentialArc({
       offset = 90,
       radius = caliperInnerEdgeRadius
     }, %)
  |> close(%)

// Revolve the brake caliiper sketch
brakeCaliper = revolve({ axis = "Y", angle = -70 }, brakeCaliperSketch)
