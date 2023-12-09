from ASCOM_functions_Dome import *
from ASCOM_functions_Telescope import *
#
#
#
#
#
# dome_base_url = 'http://localhost:32323/api/v1/dome'
# dome_number = 0
# flag = True
# #flag = False
# #Altangle=180
# Altangle=90
# Azimuth_angle=270
# #############################
# ###########################Dome connection control
#
# status=dome_connection_control(dome_base_url,dome_number,flag)
# print('Dome status :',status)
#
# ############################
# ############################Dome Altitude value
#
# Dome_altitude_value=dome_altitude_value_status(dome_base_url, dome_number)
# print('Dome_altitude_value :',Dome_altitude_value)
#
# ###########################
# ###########################Dome at home or not
#
# Dome_at_home_status=dome_at_home_status(dome_base_url, dome_number)
# print('Dome_at_home_status :',Dome_at_home_status)
#
# ###########################
# ###########################Dome at park or not
#
# Dome_at_park_status=dome_at_park_status(dome_base_url, dome_number)
# print('Dome_at_park_status :',Dome_at_park_status)
#
# ###########################
# ###########################Dome can move to home or not
#
# Dome_canMoveToHome_status=dome_can_move_to_home(dome_base_url, dome_number)
# print('Dome can move to home status :',Dome_canMoveToHome_status)
#
# ###########################
# ###########################Dome can move to home or not
#
# Dome_canPark_status=dome_can_park_or_not(dome_base_url, dome_number)
# print('Dome can park status :',Dome_canPark_status)
#
# ###########################
# ###########################Dome can set altitude or not
#
# Dome_canSetALtitude_status=dome_can_set_altitude_or_not(dome_base_url, dome_number)
# print('Dome can set altitude status :',Dome_canSetALtitude_status)
#
# ###########################
# ###########################Dome can set azimuth or not
#
# Dome_canSetAzimth_status=dome_can_set_azimuth_or_not(dome_base_url, dome_number)
# print('Dome can set azimuth status :',Dome_canSetAzimth_status)
#
# ###########################
# ###########################Dome can set park or not
#
# Dome_canSetPark_status=dome_park_can_de_set_or_not(dome_base_url, dome_number)
# print('Dome can set park status :',Dome_canSetPark_status)
#
# ###########################
# ###########################Dome shutter can open or not Auto
#
# Dome_canShutterOpen_status=dome_shutter_can_open_auto_or_not(dome_base_url, dome_number)
# print('Dome shutter can open or not Auto :',Dome_canShutterOpen_status)
#
# ###########################
# ###########################The dome support slaving to telescope
#
# Dome_canSlave_status=dome_slaving_telescope_or_not(dome_base_url, dome_number)
# print('Dome support slaving to telescope status:',Dome_canSlave_status)
#
# ###########################
# ###########################Indicate whether the dome azimuth position can be synced
#
# Dome_canAzmuthSyn_status=dome_azimuth_position_synced_or_not(dome_base_url, dome_number)
# print('Dome azimuth position can be synced status:',Dome_canAzmuthSyn_status)
#
# ###########################
# ###########################The status of the dome shutter or roll-off roof. 0 = Opened, 1 = Closed, 2 = Opening, 3 = Closing, 4 = Shutter status error
#
# Dome_shutter_status=dome_shutter_status(dome_base_url, dome_number)
# print('Dome shutter status :',Dome_shutter_status)
#
# ###########################
# ###########################Indicate whether the dome is slaved to telescope
#
# Dome_slave_status=dome_slave_status(dome_base_url, dome_number)
# print('Dome slaved to telescope :',Dome_slave_status)
#
# ###########################
# ###########################Controle dome  slaving to telescope
#
# Dome_slave_control=dome_set_slave_control(dome_base_url,dome_number, flag)
# print('Dome slaved control :',Dome_slave_control)
#
# ###########################
# ###########################indicate whether any part of dome is moving
#
# Dome_slewing_status=dome_slewing_status(dome_base_url, dome_number)
# print('Dome slewing to telescope :',Dome_slewing_status)
#
# ###########################
# ###########################immediately cancel current dome operations
#
# Dome_slewing_Control=dome_slewing_control(dome_base_url, dome_number)
# print('Dome slewing is Done :',Dome_slewing_Control)
#
# ###########################
# ###########################close shutter control
#
# Dome_shutter_closing_Control=dome_close_shutter_control(dome_base_url, dome_number)
# print('Dome shutter closing order :',Dome_shutter_closing_Control)
#
# ###########################
# ###########################Find home Control
#
# Dome_find_home_Control=dome_find_home_control(dome_base_url, dome_number)
# print('Dome Find home order :',Dome_find_home_Control)
#
# ###########################
# ###########################Open shutter control
#
# Dome_shutter_opening_Control=dome_open_shutter_control(dome_base_url, dome_number)
# print('Dome shutter opening order :',Dome_shutter_opening_Control)
#
# ###########################
# ###########################Park Dome control
#
# Dome_park_Control=dome_park_position_control(dome_base_url, dome_number)
# print('Dome Park order :',Dome_park_Control)
#
# ###########################
# ###########################Set the current azimuth, altitude position of dome to be the park position
#
# Dome_set_current_position_park_Control=dome_set_current_park_position_control(dome_base_url, dome_number)
# print('Dome set current position Park order :',Dome_set_current_position_park_Control)
#
# ###########################
# ###########################(control the altitude dome position)
#
# #I close because if you try with all above it take long time to responds if you want to test try it alone
# # Dome_set_altitude_angle=control_dome_altitude_value_motion(dome_base_url, dome_number,80)
# # print('Altitude Angle :',Dome_set_altitude_angle)
# ###########################(control the azimuth dome angle position)
#
# Dome_set_azimuth_angle=control_dome_azimuth_value_motion(dome_base_url, dome_number,Azimuth_angle)
# print('Azimth Angle :',Dome_set_azimuth_angle)
#
# ###########################(synchronize the azimuth dome angle position)control or change also the azimuth
# dome_azimuth_synch=dome_synchro_to_given_azimuth(dome_base_url, dome_number,Azimuth_angle)
# print('Azimth Angle :',dome_azimuth_synch)
#
# ###########################Actions
# action_message_response=unique_actions(dome_base_url, dome_number,'action_name')
# print(action_message_response)
#
# #############################Dome connection status
# connection_Dome_Status=connection_dome_status(dome_base_url, dome_number)
# print(connection_Dome_Status)
# ############################Dome device desciption
# device_Dome_Description=device_dome_description(dome_base_url, dome_number)
# print('Device Dome description :',device_Dome_Description)
#
# ############################Driver desciption
# Driver_Description=driver_description(dome_base_url, dome_number)
# print('Driver Description :',Driver_Description)
# ############################Driver version
# Driver_version=driver_version(dome_base_url, dome_number)
# print('Driver version :',Driver_version)
# ##########################aSCOM_device_version
# aSCOM_Device_version=aSCOM_device_version(dome_base_url, dome_number)
# print('ASCOM version :',aSCOM_Device_version)
#
# ########################device_name
# Device_name=device_name(dome_base_url, dome_number)
# print('Device name :',Device_name)
#
# ######################suported actions by the driver
# Action_name_suportted=action_name_suportted(dome_base_url, dome_number)
# print('Suported actions by the driver :',Action_name_suportted)
#
# driver_version(dome_base_url, dome_number)


###########################################################################################################
telescope_base_url = 'http://localhost:32323/api/v1/telescope'
telescope_number = 0
flag = True
axis_num=0  #0 Azmith 1 is altitude 2?
trackRate=1 #arcseconds per SI second
rateOfMotion=2 #The valid range is: , 0 to 0.6666666666666666, 1 to 2.
Declination_movement_rate_offset_degrees_sec=0.004178074616551509
rightasension_movement_rate_offset_degrees_sec=0.004178074616551509
Duration=1000#millesec range from 1 to any millesec
RAtracking_rate=1#(arcseconds per sidereal second)
mount_state=0 #0 = pierEast, 1 = pierWest
site_telescop_elevation=113#meter
site_telescop_latitude=30#deg
site_telescop_longtitiude=30#deg

RightAscension=12#hours
Declination=60#degree







SlewSettleTime=1#sec int value
Azimuth=50
Altitude=50
TrackingRate=0#The valid range is: 0 (DriveSidereal) to 3 (DriveKing)
#telescope connection control
telescope_utc_time="2023-12-09T22:29:33.1534362Z"
print(telescope_connection_control(telescope_base_url, telescope_number, flag))
print(telescope_slewing_status(telescope_base_url, telescope_number))
print(telescope_stop_slewing_control(telescope_base_url, telescope_number))
print(alignment_mood_status(telescope_base_url, telescope_number))
print(telescope_altitude_value_status(telescope_base_url, telescope_number))
print(telescope_aperture_area_value_status(telescope_base_url, telescope_number))
print(telescope_aperture_diamter_value_status(telescope_base_url, telescope_number))
print(telescope_atHome_status(telescope_base_url, telescope_number))
print(telescope_atpark_status(telescope_base_url, telescope_number))
print(telescope_axis_rate_value(telescope_base_url, telescope_number,axis_num))
print(telescope_azimuth_value(telescope_base_url, telescope_number))
print(telescope_can_findhome_or_not(telescope_base_url, telescope_number))
print(telescope_can_move_requestAxis_or_not(telescope_base_url, telescope_number,axis_num))
print(telescope_can_park_or_not(telescope_base_url, telescope_number))
print(telescope_can_pulse_guide_or_not(telescope_base_url, telescope_number))
print(telescope_can_change_dec_Rate_or_not(telescope_base_url, telescope_number))
print(telescope_can_change_guideRate_or_not(telescope_base_url, telescope_number))
print(telescope_can_SetPark_or_not(telescope_base_url, telescope_number))
print(telescope_can_SideOfPier_or_not(telescope_base_url, telescope_number))
print(telescope_can_RightAscensionRate_change_or_not(telescope_base_url, telescope_number))
print(telescope_can_Tracking_control_or_not(telescope_base_url, telescope_number))
print(telescope_can_Move_slewind_equatorial_or_not(telescope_base_url, telescope_number))
print(telescope_can_Move_slewind_AltAzim_or_not(telescope_base_url, telescope_number))
print(telescope_can_Move_slewind_localHorizontal_or_not(telescope_base_url, telescope_number))
print(telescope_can_sync_to_ALTazim_or_not(telescope_base_url, telescope_number))
print(telescope_can_unpark_or_not(telescope_base_url, telescope_number))
print(telescope_dec_value(telescope_base_url, telescope_number))
print(telescope_declination_tracking_rate_value(telescope_base_url, telescope_number))
print(telescope_delination_trackRate_control(telescope_base_url, telescope_number, trackRate))
# print(telescope__predict_pointing_state_GermanEquatorialMountvalue(telescope_base_url, telescope_number))
print(telescope_applesAtmosphereRefractioOrNot(telescope_base_url, telescope_number))
print(telescope_applyWhetherAtmosphereRefraction_control(telescope_base_url, telescope_number, flag))
print(telescope_current_applied_coordinate_sys(telescope_base_url, telescope_number))
print(telescope_home_move_control_control(telescope_base_url, telescope_number))
print(telescope_Focal_length(telescope_base_url, telescope_number))
print(telescope_DEC_movementRate(telescope_base_url, telescope_number))
print( telescope_DEC_movementRate_control(telescope_base_url, telescope_number,Declination_movement_rate_offset_degrees_sec))
print(telescope_RAS_movementRate(telescope_base_url, telescope_number))
print(telescope_RAS_movementRate_control(telescope_base_url, telescope_number,rightasension_movement_rate_offset_degrees_sec))
print(telescope_PulseGuide_status(telescope_base_url, telescope_number))
print(telescope_motion_one_axis_at_ratemotion(telescope_base_url, telescope_number,axis_num,rateOfMotion))
print(telescope_park_move_control(telescope_base_url, telescope_number))
print(telescope_rightAsension_value_status(telescope_base_url, telescope_number))
print(telescope_PULSEGUIDE(telescope_base_url, telescope_number,axis_num,Duration))
print(telescope_rightAsension_track_Rate(telescope_base_url, telescope_number))
print(telescope_rightassension_trackrate_control(telescope_base_url, telescope_number,RAtracking_rate))
print(telescope_set_park_control(telescope_base_url, telescope_number))
print(telescope_Pointing_state(telescope_base_url, telescope_number))
print(telescope_Pointing_state_control(telescope_base_url, telescope_number,mount_state))
print(telescope_siderral_time(telescope_base_url, telescope_number))
print(telescope_site_elevation_value(telescope_base_url, telescope_number))
print(telescope_site_elevation_value_control(telescope_base_url, telescope_number,site_telescop_elevation))
print(telescope_site_latitiude_value(telescope_base_url, telescope_number))
print(telescope_site_latitiude_value_control(telescope_base_url, telescope_number,site_telescop_latitude))
print(telescope_site_longtitiude_value(telescope_base_url, telescope_number))
print(telescope_site_longtitiude_value_control(telescope_base_url, telescope_number,site_telescop_longtitiude))
print(telescope_slewing_indication_any_motion_indication(telescope_base_url, telescope_number))
print(telescope_time_previous_slewing_indication(telescope_base_url, telescope_number))
print(telescope_sit_post_motion_need_time_control(telescope_base_url, telescope_number,SlewSettleTime))
print(telescope_ALTAzuth_control_sync(telescope_base_url, telescope_number,Azimuth,Altitude))
print(telescope_ALTAzuth_control_ASYNchronize(telescope_base_url, telescope_number,Azimuth,Altitude))
print(telescope_RADEC_control_sync(telescope_base_url, telescope_number,RightAscension,Declination))
print(telescope_RADEC_control_control_ASYNchronize(telescope_base_url, telescope_number,RightAscension,Declination))

print(telescope_slewtotarget_control_sync(telescope_base_url, telescope_number,RightAscension,Declination))
print(telescope_ALTAzuth_control_local_horizontal_coordinate_SYNchronize(telescope_base_url, telescope_number,Azimuth,Altitude))
print(telescope_synToCoordnate_control_sync(telescope_base_url, telescope_number,RightAscension,Declination))
print(telescope_declination_of_eqatorial_value(telescope_base_url, telescope_number))
print(telescope_SET_rightassension_equatorial_target_control(telescope_base_url, telescope_number, RightAscension))

print(telescope_SET_delination_equatorial_target_control(telescope_base_url, telescope_number, Declination))
print(telescope_is_traking_indication(telescope_base_url, telescope_number))
print(telescope_traking_control(telescope_base_url, telescope_number, flag))
print(telescope_tracking_rate_indication(telescope_base_url, telescope_number))
print(telescope_traking_rate_control(telescope_base_url, telescope_number, TrackingRate))
print(telescope_supported_DriveRates_indication(telescope_base_url, telescope_number))
print(telescope_telescope_internal_UTC_clock_indication(telescope_base_url, telescope_number))
#print(telescope_change_internal_UTC_clock_indication(telescope_base_url, telescope_number, telescope_utc_time))
print(telescope_unpark_mount_control(telescope_base_url, telescope_number))
print(telescope_connect_status(telescope_base_url, telescope_number))
print(telescope_device_description(telescope_base_url, telescope_number))
print(telescope_driver_description(telescope_base_url, telescope_number))
print(telescope_driver_version_description(telescope_base_url, telescope_number))

print(telescope_ASCOM_version(telescope_base_url, telescope_number))
print(telescope_action_lit(telescope_base_url, telescope_number))


#additional Supported actions #['AssemblyVersionNumber', 'SlewToHA', 'AvailableTimeInThisPointingState', 'TimeUntilPointingStateCanChange']supported actions

print(actions(telescope_base_url, telescope_number,'SlewToHA'))





