// Hollow Dodecahedron
// A regular dodecahedron or pentagonal dodecahedron is a dodecahedron composed of regular pentagonal faces, three meeting at each vertex. This example shows constructing the individual faces of the dodecahedron and extruding inwards.


// Input parameters
// circumscribed radius
circR = 25

// Calculated parameters
// thickness of the dodecahedron
wallThickness = circR * 0.2

// angle between faces in radians
dihedral = acos(-(sqrt(5) / 5))

// inscribed radius
inscR = circR / 15 * sqrt(75 + 30 * sqrt(5))

// pentagon edge length
edgeL = 4 * circR / (sqrt(3) * (1 + sqrt(5)))

// pentagon radius
pentR = edgeL / 2 / sin(toRadians(36))

// define a function for a polygon
fn ngon(plane, numSides, radius) {
  step = 1 / numSides * tau()
  sketch001 = startSketchOn(plane)
    |> startProfileAt([cos(0) * radius, sin(0) * radius], %)
  return reduce([1..numSides], sketch001, (i, sg) => {
      x = cos(step * i) * radius
      y = sin(step * i) * radius
      return lineTo([x, y], sg)
    })
    |> close(%)
}

// Define a plane for the bottom angled face
planeBottomSide = {
  plane = {
    origin = [
      -inscR * cos(toRadians(toDegrees(dihedral) - 90)),
      0,
      inscR - (inscR * sin(toRadians(toDegrees(dihedral) - 90)))
    ],
    xAxis = [cos(dihedral), 0.0, sin(dihedral)],
    yAxis = [0, 1, 0],
    zAxis = [sin(dihedral), 0, -cos(dihedral)]
  }
}

// Extrude the faces in each plane
bottom = extrude(wallThickness, ngon("XY", 5, pentR))
bottomSide = extrude(wallThickness, ngon(planeBottomSide, 5, pentR))

// Pattern the sides so we have a full dodecahedron
bottomBowl = patternCircular3d({
  instances = 5,
  axis = [0, 0, 1],
  center = [0, 0, 0],
  arcDegrees = 360,
  rotateDuplicates = true
}, bottomSide)

// pattern the bottom to create the top face
patternCircular3d({
  instances = 2,
  axis = [0, 1, 0],
  center = [0, 0, inscR],
  arcDegrees = 360,
  rotateDuplicates = true
}, bottom)

// pattern the bottom angled faces to create the top
patternCircular3d({
  instances = 2,
  axis = [0, 1, 0],
  center = [0, 0, inscR],
  arcDegrees = 360,
  rotateDuplicates = true
}, bottomBowl)
