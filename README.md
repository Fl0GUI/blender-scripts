These are blender scripts that I made for myself or on request. Feel free to request your own by contacting me or creating an issue on this repository. No guarantees.

# How to install
1. go to the [releases](https://github.com/Fl0GUI/blender-scripts/releases) tab and select the latest release for your blender version. Download the preferred addon zip files
2. open `blender`
3. from the `edit` menu (blender 2.8)<sup>1</sup>, open  `Preferences`, then `add-ons`
4. click `install` and select the downloaded zip file(s)

1 the user preferences in blender 2.7 are under `file`

# The scripts

### bulk blend from shape
Blends all activated Shape keys. (tbh I have no clue what this does, I'm not a blender expert)

This function can be located under the context menu of the Shape keys pane. (the little arrow under add and remove)
### custom primitives
Allows the user to store and fetch objects as if they were primitives.

This function can be found under the Add menu -> Mesh. (It should just be in the add menu since it works for more than only meshes)
### remove doubles from all
Applies the remove doubles operator on all of the objects.

This function can be found under Object from 3dview.
## How to build
1. run `$ make`
