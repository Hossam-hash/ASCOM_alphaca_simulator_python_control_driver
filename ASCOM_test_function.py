from ASCOM_functions import *





dome_base_url = 'http://localhost:32323/api/v1/dome'
dome_number = 0
flag = True
#flag = False
#Altangle=180
Altangle=90
Azimuth_angle=270
#############################
###########################Dome connection control

status=dome_connection_control(dome_base_url,dome_number,flag)
print('Dome status :',status)

############################
############################Dome Altitude value

Dome_altitude_value=dome_altitude_value_status(dome_base_url, dome_number)
print('Dome_altitude_value :',Dome_altitude_value)

###########################
###########################Dome at home or not

Dome_at_home_status=dome_at_home_status(dome_base_url, dome_number)
print('Dome_at_home_status :',Dome_at_home_status)

###########################
###########################Dome at park or not

Dome_at_park_status=dome_at_park_status(dome_base_url, dome_number)
print('Dome_at_park_status :',Dome_at_park_status)

###########################
###########################Dome can move to home or not

Dome_canMoveToHome_status=dome_can_move_to_home(dome_base_url, dome_number)
print('Dome can move to home status :',Dome_canMoveToHome_status)

###########################
###########################Dome can move to home or not

Dome_canPark_status=dome_can_park_or_not(dome_base_url, dome_number)
print('Dome can park status :',Dome_canPark_status)

###########################
###########################Dome can set altitude or not

Dome_canSetALtitude_status=dome_can_set_altitude_or_not(dome_base_url, dome_number)
print('Dome can set altitude status :',Dome_canSetALtitude_status)

###########################
###########################Dome can set azimuth or not

Dome_canSetAzimth_status=dome_can_set_azimuth_or_not(dome_base_url, dome_number)
print('Dome can set azimuth status :',Dome_canSetAzimth_status)

###########################
###########################Dome can set park or not

Dome_canSetPark_status=dome_park_can_de_set_or_not(dome_base_url, dome_number)
print('Dome can set park status :',Dome_canSetPark_status)

###########################
###########################Dome shutter can open or not Auto

Dome_canShutterOpen_status=dome_shutter_can_open_auto_or_not(dome_base_url, dome_number)
print('Dome shutter can open or not Auto :',Dome_canShutterOpen_status)

###########################
###########################The dome support slaving to telescope

Dome_canSlave_status=dome_slaving_telescope_or_not(dome_base_url, dome_number)
print('Dome support slaving to telescope status:',Dome_canSlave_status)

###########################
###########################Indicate whether the dome azimuth position can be synced

Dome_canAzmuthSyn_status=dome_azimuth_position_synced_or_not(dome_base_url, dome_number)
print('Dome azimuth position can be synced status:',Dome_canAzmuthSyn_status)

###########################
###########################The status of the dome shutter or roll-off roof. 0 = Opened, 1 = Closed, 2 = Opening, 3 = Closing, 4 = Shutter status error

Dome_shutter_status=dome_shutter_status(dome_base_url, dome_number)
print('Dome shutter status :',Dome_shutter_status)

###########################
###########################Indicate whether the dome is slaved to telescope

Dome_slave_status=dome_slave_status(dome_base_url, dome_number)
print('Dome slaved to telescope :',Dome_slave_status)

###########################
###########################Controle dome  slaving to telescope

Dome_slave_control=dome_set_slave_control(dome_base_url,dome_number, flag)
print('Dome slaved control :',Dome_slave_control)

###########################
###########################indicate whether any part of dome is moving

Dome_slewing_status=dome_slewing_status(dome_base_url, dome_number)
print('Dome slewing to telescope :',Dome_slewing_status)

###########################
###########################immediately cancel current dome operations

Dome_slewing_Control=dome_slewing_control(dome_base_url, dome_number)
print('Dome slewing is Done :',Dome_slewing_Control)

###########################
###########################close shutter control

Dome_shutter_closing_Control=dome_close_shutter_control(dome_base_url, dome_number)
print('Dome shutter closing order :',Dome_shutter_closing_Control)

###########################
###########################Find home Control

Dome_find_home_Control=dome_find_home_control(dome_base_url, dome_number)
print('Dome Find home order :',Dome_find_home_Control)

###########################
###########################Open shutter control

Dome_shutter_opening_Control=dome_open_shutter_control(dome_base_url, dome_number)
print('Dome shutter opening order :',Dome_shutter_opening_Control)

###########################
###########################Park Dome control

Dome_park_Control=dome_park_position_control(dome_base_url, dome_number)
print('Dome Park order :',Dome_park_Control)

###########################
###########################Set the current azimuth, altitude position of dome to be the park position

Dome_set_current_position_park_Control=dome_set_current_park_position_control(dome_base_url, dome_number)
print('Dome set current position Park order :',Dome_set_current_position_park_Control)

###########################
###########################(control the altitude dome position)

#I close because if you try with all above it take long time to responds if you want to test try it alone
# Dome_set_altitude_angle=control_dome_altitude_value_motion(dome_base_url, dome_number,80)
# print('Altitude Angle :',Dome_set_altitude_angle)
###########################(control the azimuth dome angle position)

Dome_set_azimuth_angle=control_dome_azimuth_value_motion(dome_base_url, dome_number,Azimuth_angle)
print('Azimth Angle :',Dome_set_azimuth_angle)

###########################(synchronize the azimuth dome angle position)control or change also the azimuth
dome_azimuth_synch=dome_synchro_to_given_azimuth(dome_base_url, dome_number,Azimuth_angle)
print('Azimth Angle :',dome_azimuth_synch)

###########################Actions
action_message_response=unique_actions(dome_base_url, dome_number,'action_name')
print(action_message_response)

#############################Dome connection status
connection_Dome_Status=connection_dome_status(dome_base_url, dome_number)
print(connection_Dome_Status)
############################Dome device desciption
device_Dome_Description=device_dome_description(dome_base_url, dome_number)
print('Device Dome description :',device_Dome_Description)

############################Driver desciption
Driver_Description=driver_description(dome_base_url, dome_number)
print('Driver Description :',Driver_Description)
############################Driver version
Driver_version=driver_version(dome_base_url, dome_number)
print('Driver version :',Driver_version)
##########################aSCOM_device_version
aSCOM_Device_version=aSCOM_device_version(dome_base_url, dome_number)
print('ASCOM version :',aSCOM_Device_version)

########################device_name
Device_name=device_name(dome_base_url, dome_number)
print('Device name :',Device_name)

######################suported actions by the driver
Action_name_suportted=action_name_suportted(dome_base_url, dome_number)
print('Suported actions by the driver :',Action_name_suportted)

driver_version(dome_base_url, dome_number)
