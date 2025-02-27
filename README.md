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
#### [3d-boaty](3d-boaty/main.kcl) ([step](step/3d-boaty.step)) ([screenshot](screenshots/3d-boaty.png))
[![3d-boaty](screenshots/3d-boaty.png)](3d-boaty/main.kcl)
#### [color-cube](color-cube/main.kcl) ([step](step/color-cube.step)) ([screenshot](screenshots/color-cube.png))
[![color-cube](screenshots/color-cube.png)](color-cube/main.kcl)
#### [enclosure](enclosure/main.kcl) ([step](step/enclosure.step)) ([screenshot](screenshots/enclosure.png))
[![enclosure](screenshots/enclosure.png)](enclosure/main.kcl)
#### [focusrite-scarlett-mounting-bracket](focusrite-scarlett-mounting-bracket/main.kcl) ([step](step/focusrite-scarlett-mounting-bracket.step)) ([screenshot](screenshots/focusrite-scarlett-mounting-bracket.png))
[![focusrite-scarlett-mounting-bracket](screenshots/focusrite-scarlett-mounting-bracket.png)](focusrite-scarlett-mounting-bracket/main.kcl)
#### [food-service-spatula](food-service-spatula/main.kcl) ([step](step/food-service-spatula.step)) ([screenshot](screenshots/food-service-spatula.png))
[![food-service-spatula](screenshots/food-service-spatula.png)](food-service-spatula/main.kcl)
#### [gear-rack](gear-rack/main.kcl) ([step](step/gear-rack.step)) ([screenshot](screenshots/gear-rack.png))
[![gear-rack](screenshots/gear-rack.png)](gear-rack/main.kcl)
#### [kitt](kitt/main.kcl) ([step](step/kitt.step)) ([screenshot](screenshots/kitt.png))
[![kitt](screenshots/kitt.png)](kitt/main.kcl)
#### [router-template-cross-bar](router-template-cross-bar/main.kcl) ([step](step/router-template-cross-bar.step)) ([screenshot](screenshots/router-template-cross-bar.png))
[![router-template-cross-bar](screenshots/router-template-cross-bar.png)](router-template-cross-bar/main.kcl)
#### [router-template-slate](router-template-slate/main.kcl) ([step](step/router-template-slate.step)) ([screenshot](screenshots/router-template-slate.png))
[![router-template-slate](screenshots/router-template-slate.png)](router-template-slate/main.kcl)
