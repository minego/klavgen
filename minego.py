import cadquery as cq

from klavgen import *

use_choc = False

# config = Config(case_config=CaseConfig(switch_type=SwitchType.CHOC, side_fillet=None, palm_rests_top_fillet=None))
# config = Config(case_config=CaseConfig())
config = Config(
	case_config=CaseConfig(
		side_fillet=7,
        switch_type=SwitchType.CHOC if use_choc else SwitchType.MX,
	),
    mx_key_config=MXKeyConfig(case_tile_margin=7.5),
    choc_key_config=ChocKeyConfig(case_tile_margin=7.6),
    controller_config=ControllerConfig(case_tile_margin=5, usb_port_hole_width=10),
)

X = CHOC_KEY_X_SPACING if use_choc else MX_KEY_X_SPACING
Y = CHOC_KEY_Y_SPACING if use_choc else MX_KEY_Y_SPACING

# keys = generate_keys_from_kle_json("../columar-split-60-left.json")
keys = [
  Key(x=0 * MX_KEY_X_SPACING, y=0.625	* - MX_KEY_Y_SPACING),
  Key(x=1 * MX_KEY_X_SPACING, y=0.375	* - MX_KEY_Y_SPACING),
  Key(x=2 * MX_KEY_X_SPACING, y=0.125	* - MX_KEY_Y_SPACING),
  Key(x=3 * MX_KEY_X_SPACING, y=0		* - MX_KEY_Y_SPACING),
  Key(x=4 * MX_KEY_X_SPACING, y=0.125	* - MX_KEY_Y_SPACING),
  Key(x=5 * MX_KEY_X_SPACING, y=0.25	* - MX_KEY_Y_SPACING),

  Key(x=0 * MX_KEY_X_SPACING, y=1.625	* - MX_KEY_Y_SPACING),
  Key(x=1 * MX_KEY_X_SPACING, y=1.375	* - MX_KEY_Y_SPACING),
  Key(x=2 * MX_KEY_X_SPACING, y=1.125	* - MX_KEY_Y_SPACING),
  Key(x=3 * MX_KEY_X_SPACING, y=1		* - MX_KEY_Y_SPACING),
  Key(x=4 * MX_KEY_X_SPACING, y=1.125	* - MX_KEY_Y_SPACING),
  Key(x=5 * MX_KEY_X_SPACING, y=1.25	* - MX_KEY_Y_SPACING),

  Key(x=0 * MX_KEY_X_SPACING, y=2.625	* - MX_KEY_Y_SPACING),
  Key(x=1 * MX_KEY_X_SPACING, y=2.375	* - MX_KEY_Y_SPACING),
  Key(x=2 * MX_KEY_X_SPACING, y=2.125	* - MX_KEY_Y_SPACING),
  Key(x=3 * MX_KEY_X_SPACING, y=2		* - MX_KEY_Y_SPACING),
  Key(x=4 * MX_KEY_X_SPACING, y=2.125	* - MX_KEY_Y_SPACING),
  Key(x=5 * MX_KEY_X_SPACING, y=2.25	* - MX_KEY_Y_SPACING),

  Key(x=0 * MX_KEY_X_SPACING, y=3.625	* - MX_KEY_Y_SPACING),
  Key(x=1 * MX_KEY_X_SPACING, y=3.375	* - MX_KEY_Y_SPACING),
  Key(x=2 * MX_KEY_X_SPACING, y=3.125	* - MX_KEY_Y_SPACING),
  Key(x=3 * MX_KEY_X_SPACING, y=3		* - MX_KEY_Y_SPACING),
  Key(x=4 * MX_KEY_X_SPACING, y=3.125	* - MX_KEY_Y_SPACING),
  Key(x=5 * MX_KEY_X_SPACING, y=3.25	* - MX_KEY_Y_SPACING),

  Key(x=1 * MX_KEY_X_SPACING, y=4.375	* - MX_KEY_Y_SPACING),
  Key(x=2 * MX_KEY_X_SPACING, y=4.125	* - MX_KEY_Y_SPACING),
  Key(x=3 * MX_KEY_X_SPACING, y=4		* - MX_KEY_Y_SPACING),
  Key(x=4 * MX_KEY_X_SPACING, y=4.125	* - MX_KEY_Y_SPACING),
  Key(x=5 * MX_KEY_X_SPACING, y=4.25	* - MX_KEY_Y_SPACING),
]

controller = Controller(x=6 * MX_KEY_X_SPACING, y=-0.8 * - MX_KEY_Y_SPACING)

screw_holes = [
	ScrewHole(x=-0.6 * MX_KEY_X_SPACING, y=-0.5 * -MX_KEY_Y_SPACING),
	ScrewHole(x= 6.8 * MX_KEY_X_SPACING, y=-0.5 * -MX_KEY_Y_SPACING),

	ScrewHole(x=-0.6 * MX_KEY_X_SPACING, y= 3.8 * -MX_KEY_Y_SPACING),
	ScrewHole(x= 6.8 * MX_KEY_X_SPACING, y= 3.8 * -MX_KEY_Y_SPACING),
]

patches = [
    Patch(
        points=[
            (-1.0 * MX_KEY_X_SPACING, -0.8 * -MX_KEY_Y_SPACING),
            (-1.0 * MX_KEY_X_SPACING,  4.3 * -MX_KEY_Y_SPACING),
            ( 0.0 * MX_KEY_X_SPACING,  5.3 * -MX_KEY_Y_SPACING),

			( 6.2 * MX_KEY_X_SPACING,  5.3 * -MX_KEY_Y_SPACING),
			( 7.2 * MX_KEY_X_SPACING,  4.3 * -MX_KEY_Y_SPACING),
			( 7.2 * MX_KEY_X_SPACING, -0.8 * -MX_KEY_Y_SPACING),
        ],
        height=config.case_config.case_base_height,
    ),

]

cuts = [
]

case_extras = [
]

keyboard_result = render_and_save_keyboard(
    keys=keys,
    screw_holes=screw_holes,
    controller=controller,
    patches=patches,
    cuts=cuts,
    case_extras=case_extras,
    debug=False,
    config=config,
)

print("Done")
