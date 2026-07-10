import cadquery as cq

from klavgen import *

use_choc = False

X = CHOC_KEY_X_SPACING if use_choc else MX_KEY_X_SPACING
Y = CHOC_KEY_Y_SPACING if use_choc else MX_KEY_Y_SPACING

# Adjusted the defaults to work with M2 threaded inserts, and M2 screws
screw_hole_config=ScrewHoleConfig(
    screw_hole_plate_radius=2.2/2,
	screw_insert_hole_width=2.8/2,
)

# nice!nano with a USB-C port
controller_config=ControllerConfig(
	case_tile_margin=5,
	usb_port_hole_width=10,
    item_depth = 35.2,
)

config_left = Config(
	case_config=CaseConfig(
		filename_prefix='left_',
		side_fillet=7,
        switch_type=SwitchType.CHOC if use_choc else SwitchType.MX,
	),
	screw_hole_config=screw_hole_config,
    mx_key_config=MXKeyConfig(case_tile_margin=7.5),
    choc_key_config=ChocKeyConfig(case_tile_margin=7.6),
    controller_config=controller_config,
)

# keys = generate_keys_from_kle_json("../columar-split-60-left.json")
keys_left = [
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

controller_left = Controller(x=6 * MX_KEY_X_SPACING, y=-0.8 * - MX_KEY_Y_SPACING)

screw_holes_left = [
	ScrewHole(x=-0.6 * MX_KEY_X_SPACING, y=-0.5 * -MX_KEY_Y_SPACING),
	ScrewHole(x= 6.8 * MX_KEY_X_SPACING, y=-0.5 * -MX_KEY_Y_SPACING),

	ScrewHole(x=-0.6 * MX_KEY_X_SPACING, y= 3.8 * -MX_KEY_Y_SPACING),
	ScrewHole(x= 6.8 * MX_KEY_X_SPACING, y= 3.8 * -MX_KEY_Y_SPACING),
]

patches_left = [
    Patch(
        points=[
            (-1.0 * MX_KEY_X_SPACING, -0.8 * -MX_KEY_Y_SPACING),
            (-1.0 * MX_KEY_X_SPACING,  4.3 * -MX_KEY_Y_SPACING),
            ( 0.0 * MX_KEY_X_SPACING,  5.3 * -MX_KEY_Y_SPACING),

			( 6.2 * MX_KEY_X_SPACING,  5.3 * -MX_KEY_Y_SPACING),
			( 7.2 * MX_KEY_X_SPACING,  4.3 * -MX_KEY_Y_SPACING),
			( 7.2 * MX_KEY_X_SPACING, -0.8 * -MX_KEY_Y_SPACING),
        ],
        height=config_left.case_config.case_base_height,
    ),

]

config_right = Config(
	case_config=CaseConfig(
		filename_prefix='right_',
		side_fillet=None,
        switch_type=SwitchType.CHOC if use_choc else SwitchType.MX,
	),
	screw_hole_config=screw_hole_config,
    mx_key_config=MXKeyConfig(case_tile_margin=7.5),
    choc_key_config=ChocKeyConfig(case_tile_margin=7.6),
    controller_config=controller_config,
)



keys_right = [
  Key(x=0 *-MX_KEY_X_SPACING, y=1.025	* - MX_KEY_Y_SPACING),
  Key(x=1 *-MX_KEY_X_SPACING, y=0.775	* - MX_KEY_Y_SPACING),
  Key(x=2 *-MX_KEY_X_SPACING, y=0.525	* - MX_KEY_Y_SPACING),
  Key(x=3 *-MX_KEY_X_SPACING, y=0.375	* - MX_KEY_Y_SPACING),
  Key(x=4 *-MX_KEY_X_SPACING, y=0.125	* - MX_KEY_Y_SPACING),
  Key(x=5 *-MX_KEY_X_SPACING, y=0		* - MX_KEY_Y_SPACING),
  Key(x=6 *-MX_KEY_X_SPACING, y=0.125	* - MX_KEY_Y_SPACING),
  Key(x=7 *-MX_KEY_X_SPACING, y=0.25	* - MX_KEY_Y_SPACING),

  Key(x=0 *-MX_KEY_X_SPACING, y=2.025	* - MX_KEY_Y_SPACING),
  Key(x=1 *-MX_KEY_X_SPACING, y=1.775	* - MX_KEY_Y_SPACING),
  Key(x=2 *-MX_KEY_X_SPACING, y=1.525	* - MX_KEY_Y_SPACING),
  Key(x=3 *-MX_KEY_X_SPACING, y=1.375	* - MX_KEY_Y_SPACING),
  Key(x=4 *-MX_KEY_X_SPACING, y=1.125	* - MX_KEY_Y_SPACING),
  Key(x=5 *-MX_KEY_X_SPACING, y=1		* - MX_KEY_Y_SPACING),
  Key(x=6 *-MX_KEY_X_SPACING, y=1.125	* - MX_KEY_Y_SPACING),
  Key(x=7 *-MX_KEY_X_SPACING, y=1.25	* - MX_KEY_Y_SPACING),

  Key(x=1 *-MX_KEY_X_SPACING, y=2.725	* - MX_KEY_Y_SPACING),
  Key(x=2 *-MX_KEY_X_SPACING, y=2.525	* - MX_KEY_Y_SPACING),
  Key(x=3 *-MX_KEY_X_SPACING, y=2.375	* - MX_KEY_Y_SPACING),
  Key(x=4 *-MX_KEY_X_SPACING, y=2.125	* - MX_KEY_Y_SPACING),
  Key(x=5 *-MX_KEY_X_SPACING, y=2		* - MX_KEY_Y_SPACING),
  Key(x=6 *-MX_KEY_X_SPACING, y=2.125	* - MX_KEY_Y_SPACING),
  Key(x=7 *-MX_KEY_X_SPACING, y=2.25	* - MX_KEY_Y_SPACING),

  Key(x=2 *-MX_KEY_X_SPACING, y=3.525	* - MX_KEY_Y_SPACING), # shift / up
  Key(x=3 *-MX_KEY_X_SPACING, y=3.375	* - MX_KEY_Y_SPACING),
  Key(x=4 *-MX_KEY_X_SPACING, y=3.125	* - MX_KEY_Y_SPACING),
  Key(x=5 *-MX_KEY_X_SPACING, y=3		* - MX_KEY_Y_SPACING),
  Key(x=6 *-MX_KEY_X_SPACING, y=3.125	* - MX_KEY_Y_SPACING),
  Key(x=7 *-MX_KEY_X_SPACING, y=3.25	* - MX_KEY_Y_SPACING),

  Key(x=1 *-MX_KEY_X_SPACING, y=4.475	* - MX_KEY_Y_SPACING), # right
  Key(x=2 *-MX_KEY_X_SPACING, y=4.475	* - MX_KEY_Y_SPACING), # down
  Key(x=3 *-MX_KEY_X_SPACING, y=4.375	* - MX_KEY_Y_SPACING), # left
  Key(x=4 *-MX_KEY_X_SPACING, y=4.125	* - MX_KEY_Y_SPACING), # ctrl
  Key(x=5 *-MX_KEY_X_SPACING, y=4		* - MX_KEY_Y_SPACING), # alt
  Key(x=6 *-MX_KEY_X_SPACING, y=4.125	* - MX_KEY_Y_SPACING), # super
  Key(x=7 *-MX_KEY_X_SPACING, y=4.25	* - MX_KEY_Y_SPACING), # space
]
controller_right = Controller(x=8 *-MX_KEY_X_SPACING, y=-0.8 * - MX_KEY_Y_SPACING)

screw_holes_right = [
	ScrewHole(x=-0.6 *-MX_KEY_X_SPACING, y=-0.5 * -MX_KEY_Y_SPACING),
	ScrewHole(x= 8.8 *-MX_KEY_X_SPACING, y=-0.5 * -MX_KEY_Y_SPACING),

	ScrewHole(x=-0.6 *-MX_KEY_X_SPACING, y= 3.8 * -MX_KEY_Y_SPACING),
	ScrewHole(x= 8.8 *-MX_KEY_X_SPACING, y= 3.8 * -MX_KEY_Y_SPACING),
]

patches_right = [
    Patch(
        points=[
            (-1.0 *-MX_KEY_X_SPACING, -0.8 * -MX_KEY_Y_SPACING),
            (-1.0 *-MX_KEY_X_SPACING,  4.3 * -MX_KEY_Y_SPACING),
            ( 0.0 *-MX_KEY_X_SPACING,  5.3 * -MX_KEY_Y_SPACING),

			( 8.2 *-MX_KEY_X_SPACING,  5.3 * -MX_KEY_Y_SPACING),
			( 9.2 *-MX_KEY_X_SPACING,  4.3 * -MX_KEY_Y_SPACING),
			( 9.2 *-MX_KEY_X_SPACING, -0.8 * -MX_KEY_Y_SPACING),
        ],
        height=config_right.case_config.case_base_height,
    ),
]

cuts = [
]

case_extras = [
]

keyboard_result = render_and_save_keyboard(
    keys=keys_left,
    screw_holes=screw_holes_left,
    controller=controller_left,
    patches=patches_left,
    cuts=cuts,
    case_extras=case_extras,
    debug=False,
    config=config_left,
)

keyboard_result = render_and_save_keyboard(
    keys=keys_right,
    screw_holes=screw_holes_right,
    controller=controller_right,
    patches=patches_right,
    cuts=cuts,
    case_extras=case_extras,
    debug=False,
    config=config_right,
)

print("Done")
