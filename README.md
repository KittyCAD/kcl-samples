# kcl-samples

KittyCAD Language (KCL) is our language for defining geometry and working with our Geometry Engine efficiently.

This repository includes a mixture of simple and complex models demonstrating the features and syntax of KCL.

The samples can be browsed in our documentation at <https://zoo.dev/docs/kcl-samples>.

## Guidelines for adding samples

Merge PRs to the `next` branch, not main. When we release Modeling App, we will merge this repo's `next` into `main`. This way, `main` is always compatible with the latest ZMA release.

KCL samples conform to a set of style guidelines to ensure consistency and readability.

1. **File Naming:** Name your KCL files descriptively and concisely, using hyphens to separate words (e.g., flange.kcl, ball-bearing.kcl).

2. **File Header:** Include a title comment at the top of each file, followed by a brief description explaining what the model is and its typical use cases.

3. **Inline Comments:** Use inline comments to explain non-obvious parts of the code. Each major section should have a comment describing its purpose.

4. **Constants:** Define constants at the beginning of your KCL files for any values that might change or need to be reused (e.g., dimensions, angles).

## Snapshot and export

When you submit a PR to add or modify KCL samples, images and STEP files will be generated and added to the repository automatically.

---
#### [a-parametric-bearing-pillow-block](a-parametric-bearing-pillow-block/main.kcl) ([step](step/a-parametric-bearing-pillow-block.step)) ([screenshot](screenshots/a-parametric-bearing-pillow-block.png))
[![a-parametric-bearing-pillow-block](screenshots/a-parametric-bearing-pillow-block.png)](a-parametric-bearing-pillow-block/main.kcl)
#### [ball-bearing](ball-bearing/main.kcl) ([step](step/ball-bearing.step)) ([screenshot](screenshots/ball-bearing.png))
[![ball-bearing](screenshots/ball-bearing.png)](ball-bearing/main.kcl)
#### [bracket](bracket/main.kcl) ([step](step/bracket.step)) ([screenshot](screenshots/bracket.png))
[![bracket](screenshots/bracket.png)](bracket/main.kcl)
#### [color-cube](color-cube/main.kcl) ([step](step/color-cube.step)) ([screenshot](screenshots/color-cube.png))
[![color-cube](screenshots/color-cube.png)](color-cube/main.kcl)
#### [cycloidal-gear](cycloidal-gear/main.kcl) ([step](step/cycloidal-gear.step)) ([screenshot](screenshots/cycloidal-gear.png))
[![cycloidal-gear](screenshots/cycloidal-gear.png)](cycloidal-gear/main.kcl)
#### [dodecahedron](dodecahedron/main.kcl) ([step](step/dodecahedron.step)) ([screenshot](screenshots/dodecahedron.png))
[![dodecahedron](screenshots/dodecahedron.png)](dodecahedron/main.kcl)
#### [enclosure](enclosure/main.kcl) ([step](step/enclosure.step)) ([screenshot](screenshots/enclosure.png))
[![enclosure](screenshots/enclosure.png)](enclosure/main.kcl)
#### [flange-with-patterns](flange-with-patterns/main.kcl) ([step](step/flange-with-patterns.step)) ([screenshot](screenshots/flange-with-patterns.png))
[![flange-with-patterns](screenshots/flange-with-patterns.png)](flange-with-patterns/main.kcl)
#### [flange-xy](flange-xy/main.kcl) ([step](step/flange-xy.step)) ([screenshot](screenshots/flange-xy.png))
[![flange-xy](screenshots/flange-xy.png)](flange-xy/main.kcl)
#### [focusrite-scarlett-mounting-bracket](focusrite-scarlett-mounting-bracket/main.kcl) ([step](step/focusrite-scarlett-mounting-bracket.step)) ([screenshot](screenshots/focusrite-scarlett-mounting-bracket.png))
[![focusrite-scarlett-mounting-bracket](screenshots/focusrite-scarlett-mounting-bracket.png)](focusrite-scarlett-mounting-bracket/main.kcl)
#### [gear-rack](gear-rack/main.kcl) ([step](step/gear-rack.step)) ([screenshot](screenshots/gear-rack.png))
[![gear-rack](screenshots/gear-rack.png)](gear-rack/main.kcl)
#### [hex-nut](hex-nut/main.kcl) ([step](step/hex-nut.step)) ([screenshot](screenshots/hex-nut.png))
[![hex-nut](screenshots/hex-nut.png)](hex-nut/main.kcl)
#### [kitt](kitt/main.kcl) ([step](step/kitt.step)) ([screenshot](screenshots/kitt.png))
[![kitt](screenshots/kitt.png)](kitt/main.kcl)
#### [lego](lego/main.kcl) ([step](step/lego.step)) ([screenshot](screenshots/lego.png))
[![lego](screenshots/lego.png)](lego/main.kcl)
#### [mounting-plate](mounting-plate/main.kcl) ([step](step/mounting-plate.step)) ([screenshot](screenshots/mounting-plate.png))
[![mounting-plate](screenshots/mounting-plate.png)](mounting-plate/main.kcl)
#### [multi-axis-robot](multi-axis-robot/main.kcl) ([step](step/multi-axis-robot.step)) ([screenshot](screenshots/multi-axis-robot.png))
[![multi-axis-robot](screenshots/multi-axis-robot.png)](multi-axis-robot/main.kcl)
#### [pipe-with-bend](pipe-with-bend/main.kcl) ([step](step/pipe-with-bend.step)) ([screenshot](screenshots/pipe-with-bend.png))
[![pipe-with-bend](screenshots/pipe-with-bend.png)](pipe-with-bend/main.kcl)
#### [sheet-metal-bracket](sheet-metal-bracket/main.kcl) ([step](step/sheet-metal-bracket.step)) ([screenshot](screenshots/sheet-metal-bracket.png))
[![sheet-metal-bracket](screenshots/sheet-metal-bracket.png)](sheet-metal-bracket/main.kcl)
#### [washer](washer/main.kcl) ([step](step/washer.step)) ([screenshot](screenshots/washer.png))
[![washer](screenshots/washer.png)](washer/main.kcl)
