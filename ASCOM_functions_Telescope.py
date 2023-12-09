

import requests
telescope_base_url = 'http://localhost:32323/api/v1/telescope'
telescope_number = 0
flag = True


def telescope_connection_control(telescop_base_url, telescope_number, flag):
    """control the connection of telescope flag=true make connection true and the oppsite is true """
    url = f"{telescop_base_url}/{str(telescope_number)}/connected"
    data = {'Connected': str(flag)}
    response = requests.put(url, data=data)
    status = requests.get(url)
    if status.json()['Value']==True:
        return 'telescope is connected'
    else:
        return 'telescope is Disconnected'

def telescope_connect_status(telescope_base_url, telescope_number):
    '''Retrieves the connected state of the device'''
    url= f"{telescope_base_url}/{str(telescope_number)}/connected?"
    return requests.get(url).json()['Value']




def telescope_device_description(telescope_base_url, telescope_number):
    '''The description of the device'''
    url= f"{telescope_base_url}/{str(telescope_number)}/description?"
    return requests.get(url).json()['Value']

def telescope_driver_description(telescope_base_url, telescope_number):
    '''The description of the driver'''
    url= f"{telescope_base_url}/{str(telescope_number)}/driverinfo?"
    return requests.get(url).json()['Value']


def telescope_driver_version_description(telescope_base_url, telescope_number):
    '''The description of the driver version'''
    url= f"{telescope_base_url}/{str(telescope_number)}/driverversion?"
    return requests.get(url).json()['Value']

def telescope_ASCOM_version(telescope_base_url, telescope_number):
    '''This method returns the version of the ASCOM device interface contract to which this device complies. Only one interface version is current at a moment in time and all new devices should be built to the latest interface version. Applications can choose which device interface versions they support and it is in their interest to support previous versions as well as the current version to ensure they can use the largest number of devices.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/interfaceversion?"
    return requests.get(url).json()['Value']


def telescope_action_lit(telescope_base_url, telescope_number):
    '''Returns the list of action names supported by this driver.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/supportedactions?"
    return requests.get(url).json()['Value']






def telescope_slewing_status(telescope_base_url, telescope_number):
    '''True if telescope is currently moving in response to one of the Slew methods or the MoveAxis(TelescopeAxes, Double) method, False at all other times.'''
    tele_slewing_Status= f"{telescope_base_url}/{str(telescope_number)}/slewing?"
    return requests.get(tele_slewing_Status).json()['Value']

def telescope_stop_slewing_control(telescope_base_url, telescope_number):
    '''Immediately Stops a slew in progress..Calling this method will immediately disable hardware slewing (Slaved will become False).immediately cancel current telescope operations'''
    tele_slewing_Control= f"{telescope_base_url}/{str(telescope_number)}/abortslew?"
    if telescope_slewing_status(telescope_base_url, telescope_number)==True:
        if requests.put(tele_slewing_Control).status_code==200:
            return 'Dome is slaved (Stoped)'
        else:
            return requests.put(tele_slewing_Control).json()['ErrorMessage']
    else:
        return 'telescope is not move (isnot slewing)'

def alignment_mood_status(telescope_base_url, telescope_number):
    '''Returns the alignment mode of the mount (Alt/Az{0}, Polar(Equatorial){1}, German Polar{2}). The alignment mode is specified as an integer value from the AlignmentModes Enum.'''
    tele_alignment_mood_status= f"{telescope_base_url}/{str(telescope_number)}/alignmentmode?"
    return requests.get(tele_alignment_mood_status).json()['Value']


def telescope_altitude_value_status(telescope_base_url, telescope_number):
    '''The altitude above the local horizon of the mount's current position (degrees, positive up) even it equatorial or altazimuth'''
    tele_altiude_url= f"{telescope_base_url}/{str(telescope_number)}/altitude?"
    return requests.get(tele_altiude_url).json()['Value']

def telescope_aperture_area_value_status(telescope_base_url, telescope_number):
    '''The area of the telescope's aperture, taking into account any obstructions (square meters)'''
    tele_app_area_url= f"{telescope_base_url}/{str(telescope_number)}/aperturearea?"
    return requests.get(tele_app_area_url).json()['Value']

'''The telescope's effective aperture diameter (meters)'''

def telescope_aperture_diamter_value_status(telescope_base_url, telescope_number):
    '''The area of the telescope's aperture, taking into account any obstructions (square meters)'''
    tele_app_diameter_url= f"{telescope_base_url}/{str(telescope_number)}/aperturediameter?"
    return requests.get(tele_app_diameter_url).json()['Value']


def telescope_atHome_status(telescope_base_url, telescope_number):
    '''True if the mount is stopped in the Home position. Set only following a FindHome() operation, and reset with any slew operation. This property must be False if the telescope does not support homing.'''
    tele_athome_url= f"{telescope_base_url}/{str(telescope_number)}/athome?"
    return requests.get(tele_athome_url).json()['Value']


def telescope_atpark_status(telescope_base_url, telescope_number):
    '''True if the telescope has been put into the parked state by the see Park() method. Set False by calling the Unpark() method.'''
    tele_atpark_url= f"{telescope_base_url}/{str(telescope_number)}/atpark?"
    return requests.get(tele_atpark_url).json()['Value']

def telescope_axis_rate_value(telescope_base_url, telescope_number,axis_num):
    '''The rates at which the telescope may be moved about the specified axis by the MoveAxis(TelescopeAxes, Double) method.'''
    '''The axis about which rate information is desired. 0 = axisPrimary, 1 = axisSecondary, 2 = axisTertiary.'''
    tele_axisRate_url = f"{telescope_base_url}/{str(telescope_number)}/axisrates?Axis={axis_num}"
    if 0<=axis_num<=2:
        return requests.get(tele_axisRate_url).json()['Value']
    else:
        return 'Error axis_num =0 or 1 or 2 '


def telescope_azimuth_value(telescope_base_url, telescope_number):
    '''The azimuth at the local horizon of the mount's current position (degrees, North-referenced, positive East/clockwise).'''
    tele_AZvalatpark_url= f"{telescope_base_url}/{str(telescope_number)}/azimuth?"
    return requests.get(tele_AZvalatpark_url).json()['Value']


def telescope_can_findhome_or_not(telescope_base_url, telescope_number):
    '''True if this telescope is capable of programmed finding its home position (FindHome() method).'''
    tele_canFindHome_url= f"{telescope_base_url}/{str(telescope_number)}/canfindhome?"
    return requests.get(tele_canFindHome_url).json()['Value']

def telescope_can_move_requestAxis_or_not(telescope_base_url, telescope_number,axis_num):
    '''True if this telescope can move the requested axis'''
    '''The axis about which rate information is desired. 0 = axisPrimary, 1 = axisSecondary, 2 = axisTertiary.'''
    tele_can_move_requestAxis_url= f"{telescope_base_url}/{str(telescope_number)}/canmoveaxis?Axis={axis_num}"
    return requests.get(tele_can_move_requestAxis_url).json()['Value']


def telescope_can_park_or_not(telescope_base_url, telescope_number):
    '''True if this telescope is capable of programmed parking (Park() method)'''
    tele_canPark_url= f"{telescope_base_url}/{str(telescope_number)}/canpark?"
    return requests.get(tele_canPark_url).json()['Value']


def telescope_can_pulse_guide_or_not(telescope_base_url, telescope_number):
    '''True if this telescope is capable of software-pulsed guiding (via the PulseGuide(GuideDirections, Int32) method)'''
    tele_canpulse_guide_url= f"{telescope_base_url}/{str(telescope_number)}/canpulseguide?"
    return requests.get(tele_canpulse_guide_url).json()['Value']

def telescope_can_change_dec_Rate_or_not(telescope_base_url, telescope_number):
    '''True if the DeclinationRate property can be changed to provide offset tracking in the declination axis.'''
    tele_can_change_dec_Rate_url= f"{telescope_base_url}/{str(telescope_number)}/cansetdeclinationrate?"
    return requests.get(tele_can_change_dec_Rate_url).json()['Value']

def telescope_can_change_guideRate_or_not(telescope_base_url, telescope_number):
    '''True if the guide rate properties used for PulseGuide(GuideDirections, Int32) can be adjusted.'''
    tele_can_change_guideRate_url= f"{telescope_base_url}/{str(telescope_number)}/cansetguiderates?"
    return requests.get(tele_can_change_guideRate_url).json()['Value']


def telescope_can_SetPark_or_not(telescope_base_url, telescope_number):
    '''True if this telescope is capable of programmed setting of its park position (SetPark() method)'''
    url= f"{telescope_base_url}/{str(telescope_number)}/cansetpark?"
    return requests.get(url).json()['Value']

def telescope_can_SideOfPier_or_not(telescope_base_url, telescope_number):
    '''True if the SideOfPier property can be set, meaning that the mount can be forced to flip. can flip ro not az=+90'''
    url= f"{telescope_base_url}/{str(telescope_number)}/cansetpierside?"
    return requests.get(url).json()['Value']


def telescope_can_RightAscensionRate_change_or_not(telescope_base_url, telescope_number):
    '''True if the RightAscensionRate property can be changed to provide offset tracking in the right ascension axis'''
    url= f"{telescope_base_url}/{str(telescope_number)}/cansetrightascensionrate?"
    return requests.get(url).json()['Value']

def telescope_can_Tracking_control_or_not(telescope_base_url, telescope_number):
    '''True if the Tracking property can be changed, turning telescope sidereal tracking on and off.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/cansettracking?"
    return requests.get(url).json()['Value']


def telescope_can_Move_slewind_equatorial_or_not(telescope_base_url, telescope_number):
    '''True if this telescope is capable of programmed slewing (synchronous or asynchronous) to equatorial coordinates'''
    url= f"{telescope_base_url}/{str(telescope_number)}/canslew?"
    return requests.get(url).json()['Value']

def telescope_can_Move_slewind_AltAzim_or_not(telescope_base_url, telescope_number):
    '''True if this telescope is capable of programmed slewing (synchronous or asynchronous) to local horizontal coordinates'''
    url= f"{telescope_base_url}/{str(telescope_number)}/canslewaltaz?"
    return requests.get(url).json()['Value']

def telescope_can_Move_slewind_localHorizontal_or_not(telescope_base_url, telescope_number):
    '''True if this telescope is capable of programmed asynchronous slewing to local horizontal coordinates'''
    url= f"{telescope_base_url}/{str(telescope_number)}/canslewaltazasync?"
    return requests.get(url).json()['Value']


def telescope_can_sync_to_equatorial_or_not(telescope_base_url, telescope_number):
    '''True if this telescope is capable of programmed syncing to equatorial coordinates.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/cansync?"
    return requests.get(url).json()['Value']




def telescope_can_sync_to_ALTazim_or_not(telescope_base_url, telescope_number):
    '''True if this telescope is capable of programmed syncing to ALTAZim coordinates.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/cansyncaltaz?"
    return requests.get(url).json()['Value']

def telescope_can_unpark_or_not(telescope_base_url, telescope_number):
    '''True if this telescope is capable of programmed unparking (Unpark() method)'''
    url= f"{telescope_base_url}/{str(telescope_number)}/canunpark?"
    return requests.get(url).json()['Value']


def telescope_dec_value(telescope_base_url, telescope_number):
    '''The declination (degrees) of the mount's current equatorial coordinates, in the coordinate system given by the EquatorialSystem property. Reading the property will raise an error if the value is unavailable.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/declination?"
    return requests.get(url).json()['Value']

def telescope_declination_of_eqatorial_value(telescope_base_url, telescope_number):
    '''The declination (degrees, positive North) for the target of an equatorial slew or sync operation the current target dec'''
    url= f"{telescope_base_url}/{str(telescope_number)}/targetdeclination?"
    return requests.get(url).json()['Value']


def telescope_rightassension_of_eqatorial_value(telescope_base_url, telescope_number):
    '''The right ascension (hours) for the target of an equatorial slew or sync operation'''
    url= f"{telescope_base_url}/{str(telescope_number)}/targetrightascension?"
    return requests.get(url).json()['Value']



def telescope_SET_rightassension_equatorial_target_control(telescope_base_url, telescope_number, RightAscension):
    '''Sets the right ascension (hours) for the target of an equatorial slew or sync operation
    "TargetRightAscension set - '50' is an invalid value. The valid range is: 0 to 24."'''

    url = f"{telescope_base_url}/{str(telescope_number)}/targetrightascension"
    data = {'TargetRightAscension': RightAscension}
    response = requests.put(url, data=data)
    if response.status_code == 200:
        return f"{'rigtassension Changed'}"
    else:
        return 'ErrorMessage'
def telescope_SET_delination_equatorial_target_control(telescope_base_url, telescope_number, Declination):
    '''Sets the declination (degrees, positive North) for the target of an equatorial slew or sync operation'''

    url = f"{telescope_base_url}/{str(telescope_number)}/targetdeclination"
    data = {'TargetDeclination': Declination}
    response = requests.put(url, data=data)
    if response.status_code == 200:
        return f"{'Declination Changed'}"
    else:
        return 'ErrorMessage'



def telescope_declination_tracking_rate_value(telescope_base_url, telescope_number):
    '''The declination tracking rate (arcseconds per SI second, default = 0.0). Please note that rightascensionrate units are arcseconds per sidereal second.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/declinationrate?"
    return requests.get(url).json()['Value']



def telescope_delination_trackRate_control(telescope_base_url, telescope_number, trackRate):
    '''Sets the declination tracking rate (arcseconds per SI second). Please note that rightascensionrate units are arcseconds per sidereal second.
    Declination tracking rate (arcseconds per SI second). Please note that rightascensionrate units are arcseconds per sidereal second.
    '''
    url = f"{telescope_base_url}/{str(telescope_number)}/declinationrate"
    data = {'DeclinationRate': str(trackRate)}
    response = requests.put(url, data=data)
    status = requests.get(url)
    if response.status_code == 200:
        return f"{'DeclinationRate Changed'}/{status.json()['Value']}"
    else:
        return status.json()['ErrorMessage']



# def telescope__predict_pointing_state_GermanEquatorialMountvalue(telescope_base_url, telescope_number):
#     '''Predicts the pointing state that a German equatorial mount will be in if it slews to the given coordinates. The return value will be one of - 0 = pierEast, 1 = pierWest, -1 = pierUnknown'''
#     url= f"{telescope_base_url}/{str(telescope_number)}/destinationsideofpier"
#     return requests.get(url).text

def telescope_applesAtmosphereRefractioOrNot(telescope_base_url, telescope_number):
    '''True if the telescope or driver applies atmospheric refraction to coordinates.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/doesrefraction?"
    return requests.get(url).json()['Value']



def telescope_applyWhetherAtmosphereRefraction_control(telescope_base_url, telescope_number, flag):
    '''Determines whether atmospheric refraction is applied to coordinates.'''
    url = f"{telescope_base_url}/{str(telescope_number)}/doesrefraction"
    data = {'DoesRefraction': str(flag)}
    response = requests.put(url, data=data)
    status = requests.get(url)
    if response.status_code == 200:
        return f"{'telescope or driver applies atmospheric refraction Done'}/{status.json()['Value']}"
    else:
        return status.json()['ErrorMessage']


def telescope_current_applied_coordinate_sys(telescope_base_url, telescope_number):
    '''Returns the current equatorial coordinate system used by this telescope (e.g. Topocentric or J2000)
    0=local
    1=B1950
    2=j2000
    3=j250
    4=others
    '''
    url= f"{telescope_base_url}/{str(telescope_number)}/equatorialsystem?"
    return requests.get(url).json()['Value']




def telescope_home_move_control_control(telescope_base_url, telescope_number):
    '''move the mount to home Locates the telescope's "home" position (synchronous)'''
    url = f"{telescope_base_url}/{str(telescope_number)}/findhome"
    response = requests.put(url)
    if response.status_code == 200:
        return 'Telescope is at Home'




def telescope_Focal_length(telescope_base_url, telescope_number):
    '''Return The telescope's focal length in meters'''
    url= f"{telescope_base_url}/{str(telescope_number)}/focallength?"
    return requests.get(url).json()['Value']


def telescope_DEC_movementRate(telescope_base_url, telescope_number):
    '''The current Declination movement rate offset for telescope guiding (degrees/sec)'''
    url= f"{telescope_base_url}/{str(telescope_number)}/guideratedeclination?"
    return requests.get(url).json()['Value']



def telescope_DEC_movementRate_control(telescope_base_url, telescope_number,Declination_movement_rate_offset_degrees_sec):
    '''Sets the current Declination movement rate offset for telescope guiding (degrees/sec).'''
    url = f"{telescope_base_url}/{str(telescope_number)}/guideratedeclination"
    data = {'GuideRateDeclination': Declination_movement_rate_offset_degrees_sec}
    response = requests.put(url, data=data)
    status = requests.get(url)
    if response.status_code == 200:
        return f"{'The current Declination movement rate offset for telescope guiding (degrees/sec) :'}/{telescope_DEC_movementRate(telescope_base_url, telescope_number)}"
    else:
        return status.json()['ErrorMessage']




def telescope_RAS_movementRate(telescope_base_url, telescope_number):
    '''The current RightAscension movement rate offset for telescope guiding (degrees/sec)'''
    url= f"{telescope_base_url}/{str(telescope_number)}/guideraterightascension?"
    return requests.get(url).json()['Value']

def telescope_RAS_movementRate_control(telescope_base_url, telescope_number,rightasension_movement_rate_offset_degrees_sec):
    '''Sets the current RightAscension movement rate offset for telescope guiding (degrees/sec).'''
    url = f"{telescope_base_url}/{str(telescope_number)}/guideraterightascension"
    data = {'GuideRateRightAscension': rightasension_movement_rate_offset_degrees_sec}
    response = requests.put(url, data=data)
    status = requests.get(url)
    if response.status_code == 200:
        return f"{'The current RightAsension movement rate offset for telescope guiding (degrees/sec) :'}/{telescope_RAS_movementRate(telescope_base_url, telescope_number)}"
    else:
        return status.json()['ErrorMessage']



def telescope_PulseGuide_status(telescope_base_url, telescope_number):
    '''True if a PulseGuide(GuideDirections, Int32) command is in progress, False otherwise'''
    url= f"{telescope_base_url}/{str(telescope_number)}/ispulseguiding?"
    return requests.get(url).json()['Value']


#important
def telescope_motion_one_axis_at_ratemotion(telescope_base_url, telescope_number,axis_no,rateOfMotion):
    '''Move the telescope in one axis at the given rate.motion of telescope
    . The valid range is: , 0 to 0.6666666666666666, 1 to 2.
    The rate of motion (deg/sec) about the specified axis'''
    url = f"{telescope_base_url}/{str(telescope_number)}/moveaxis"
    data = {'Axis': axis_no,
            'Rate': rateOfMotion,
            }
    response = requests.put(url, data=data)
    if response.status_code == 200:
        return f"{'Moving at rate motion :'}{rateOfMotion} (deg/sec)"
    else:
        return response.json()['ErrorMessage']


def telescope_park_move_control(telescope_base_url, telescope_number):
    '''Move the telescope to its park position, stop all motion (or restrict to a small safe range), and set AtPark to True.'''
    url = f"{telescope_base_url}/{str(telescope_number)}/park"
    response = requests.put(url)
    if response.status_code == 200:
        return 'Telescope set the Parked position here'


def telescope_rightAsension_value_status(telescope_base_url, telescope_number):
    '''The right ascension (hours) of the mount's current equatorial coordinates, in the coordinate system given by the EquatorialSystem property'''
    tele_altiude_url= f"{telescope_base_url}/{str(telescope_number)}/rightascension?"
    return requests.get(tele_altiude_url).json()['Value']


#######important
def telescope_PULSEGUIDE(telescope_base_url, telescope_number,axis_num,Duration):
    '''Moves the scope in the given direction for the given interval or time at the rate given by the corresponding guide rate property
    Duration IN millisec >=1
    axis_no 0,1,2,3 az,alt,ra,dec

    '''

    url = f"{telescope_base_url}/{str(telescope_number)}/pulseguide"
    data = {'Direction': int(axis_num),
            'Duration': int(Duration),
            }
    az=telescope_azimuth_value(telescope_base_url, telescope_number)
    alt=telescope_altitude_value_status(telescope_base_url, telescope_number)
    ra=telescope_rightAsension_value_status(telescope_base_url, telescope_number)
    dec=telescope_dec_value(telescope_base_url, telescope_number)
    response = requests.put(url, data=data)
    if response.status_code == 200:
        if axis_num==0:
            return f"{'Past Azimuth :'}{az}{'---New Azimuth :'}{telescope_azimuth_value(telescope_base_url, telescope_number)} (deg)"
        elif axis_num==1:
            return f"{'Past Altitude :'}{alt}{'---New Altitude :'}{telescope_altitude_value_status(telescope_base_url, telescope_number)} (deg)"
        elif axis_num==2:
            return f"{'Past rightAsension :'}{ra}{'---New rightAsension :'}{telescope_rightAsension_value_status(telescope_base_url, telescope_number)} "
        elif axis_num==3:
            return f"{'Past Declination :'}{dec}{'---New Declination :'}{telescope_dec_value(telescope_base_url, telescope_number)} "
    else:
        return 'Error'



def telescope_rightAsension_track_Rate(telescope_base_url, telescope_number):
    '''The right ascension tracking rate (arcseconds per sidereal second, default = 0.0). Please note that the declinationrate units are arcseconds per SI second.'''
    tele_altiude_url= f"{telescope_base_url}/{str(telescope_number)}/rightascensionrate?"
    return requests.get(tele_altiude_url).json()['Value']




def telescope_rightassension_trackrate_control(telescope_base_url, telescope_number,RAtracking_rate):
    '''Sets the right ascension tracking rate (arcseconds per sidereal second). Please note that the declinationrate units are arcseconds per SI second'''
    url = f"{telescope_base_url}/{str(telescope_number)}/rightascensionrate"
    data = {'RightAscensionRate': int(RAtracking_rate)}
    response = requests.put(url, data=data)
    #status = requests.get(url)
    if response.status_code == 200:
        return f"{'the right ascension tracking rate (arcseconds per sidereal second) :'}/{telescope_rightAsension_track_Rate(telescope_base_url, telescope_number)}"
    else:
        return 'ErrorMessage'


def telescope_set_park_control(telescope_base_url, telescope_number):
    '''Sets the telescope's park position to be its current position.'''
    url = f"{telescope_base_url}/{str(telescope_number)}/setpark"
    response = requests.put(url)
    if response.status_code == 200:
        return 'Telescope is Parked'


def telescope_Pointing_state(telescope_base_url, telescope_number):
    '''Indicates the pointing state of the mount. 0 = pierEast, 1 = pierWest, -1= pierUnknown'''
    url= f"{telescope_base_url}/{str(telescope_number)}/sideofpier?"
    return requests.get(url).json()['Value']



def telescope_Pointing_state_control(telescope_base_url, telescope_number,mount_state):
    '''Sets the pointing state of the mount. 0 = pierEast, 1 = pierWest'''
    url = f"{telescope_base_url}/{str(telescope_number)}/sideofpier"
    if int(mount_state)==0 or int(mount_state)==1 :
        data = {'SideOfPier': int(mount_state)}
        response = requests.put(url, data=data)
        #status = requests.get(url)
        if response.status_code == 200:
            return f"{'the pointing state of the mount. 0 = pierEast, 1 = pierWest, -1= pierUnknown :'}/{telescope_Pointing_state(telescope_base_url, telescope_number)}"
    else:
        return 'mount_state = 0 or 1 else error'


def telescope_siderral_time(telescope_base_url, telescope_number):
    '''The local apparent sidereal time from the telescope's internal clock (hours, sidereal).The local apparent sidereal time from the telescope's internal clock (hours, sidereal).'''
    url= f"{telescope_base_url}/{str(telescope_number)}/siderealtime?"
    return requests.get(url).json()['Value']


def telescope_site_elevation_value(telescope_base_url, telescope_number):
    '''The elevation above mean sea level (meters) of the site at which the telescope is located.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/siteelevation?"
    return requests.get(url).json()['Value']


def telescope_site_elevation_value_control(telescope_base_url, telescope_number,site_telescop_elevation):
    '''Sets the elevation above mean sea level (metres) of the site at which the telescope is located.'''
    url = f"{telescope_base_url}/{str(telescope_number)}/siteelevation"
    data = {'SiteElevation': site_telescop_elevation}
    response = requests.put(url, data=data)
    #status = requests.get(url)
    if response.status_code == 200:
        return f"{'the site at which the telescope is located meter :'}/{telescope_site_elevation_value(telescope_base_url, telescope_number)}"
    else:
        return 'ErrorMessage'


def telescope_site_latitiude_value(telescope_base_url, telescope_number):
    '''The geodetic(map) latitude (degrees, positive North, WGS84) of the site at which the telescope is located.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/sitelatitude?"
    return requests.get(url).json()['Value']




def telescope_site_latitiude_value_control(telescope_base_url, telescope_number,site_telescop_latitude):
    '''Sets the observing site's latitude (degrees).'''
    url = f"{telescope_base_url}/{str(telescope_number)}/sitelatitude"
    data = {'SiteLatitude': site_telescop_latitude}
    response = requests.put(url, data=data)
    #status = requests.get(url)
    if response.status_code == 200:
        return f"{'the observing sites latitude (degrees) :'}/{telescope_site_latitiude_value(telescope_base_url, telescope_number)}"
    else:
        return 'ErrorMessage'



def telescope_site_longtitiude_value(telescope_base_url, telescope_number):
    '''The longitude (degrees, positive East, WGS84) of the site at which the telescope is located.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/sitelongitude?"
    return requests.get(url).json()['Value']


def telescope_site_longtitiude_value_control(telescope_base_url, telescope_number,site_telescop_longtitiude):
    '''Sets the observing site's longitude (degrees, positive East, WGS84).'''
    url = f"{telescope_base_url}/{str(telescope_number)}/sitelongitude"
    data = {'SiteLongitude': site_telescop_longtitiude}
    response = requests.put(url, data=data)
    #status = requests.get(url)
    if response.status_code == 200:
        return f"{'the observing sites longtitiude (degrees) :'}/{telescope_site_longtitiude_value(telescope_base_url, telescope_number)}"
    else:
        return 'ErrorMessage'

def telescope_slewing_indication_any_motion_indication(telescope_base_url, telescope_number):
    '''True if telescope is currently moving in response to one of the Slew methods or the MoveAxis(TelescopeAxes, Double) method, False at all other times'''
    url= f"{telescope_base_url}/{str(telescope_number)}/slewing?"
    return requests.get(url).json()['Value']

#important
def telescope_time_previous_slewing_indication(telescope_base_url, telescope_number):
    '''Returns the post-slew settling time (sec.).'''
    url= f"{telescope_base_url}/{str(telescope_number)}/slewsettletime?"
    return requests.get(url).json()['Value']



def telescope_sit_post_motion_need_time_control(telescope_base_url, telescope_number,SlewSettleTime):
    '''Sets the post-slew settling time (integer sec.).'''
    url = f"{telescope_base_url}/{str(telescope_number)}/slewsettletime"
    data = {'SlewSettleTime': int(SlewSettleTime)}
    response = requests.put(url, data=data)
    #status = requests.get(url)
    if response.status_code == 200:
        return f"{'ts of post motion :'}/{telescope_time_previous_slewing_indication(telescope_base_url, telescope_number)}"
    else:
        return 'ErrorMessage'

#important
def telescope_ALTAzuth_control_sync(telescope_base_url, telescope_number,Azimuth,Altitude):
    '''Move the telescope to the given local horizontal coordinates, return when slew is complete synchronizly move to given coordnate'''
    url = f"{telescope_base_url}/{str(telescope_number)}/slewtoaltaz"
    data = {'Azimuth': Azimuth,
            'Altitude': Altitude,
            }
    response = requests.put(url, data=data)
    #status = requests.get(url)
    if response.status_code == 200:
        return f"{'ts of post motion :'}/{telescope_time_previous_slewing_indication(telescope_base_url, telescope_number)}{' Alt='}{telescope_altitude_value_status(telescope_base_url, telescope_number)}{' Azmuth='}{telescope_azimuth_value(telescope_base_url, telescope_number)}"
    else:
        return 'ErrorMessage'



#important
def telescope_ALTAzuth_control_ASYNchronize(telescope_base_url, telescope_number,Azimuth,Altitude):
    '''Move the telescope to the given local horizontal coordinates, return immediately after the slew starts. The client can poll the Slewing method to determine when the mount reaches the intended coordinates.
     this command is asking the telescope to move to specific coordinates in the local horizontal system, and the client can continue with other tasks immediately. The client can periodically check the Slewing status to know when the telescope has reached the intended coordinates. This asynchronous approach allows the client to perform other operations while the telescope is in motion
    '''
    url = f"{telescope_base_url}/{str(telescope_number)}/slewtoaltazasync"
    data = {'Azimuth': Azimuth,
            'Altitude': Altitude,
            }
    response = requests.put(url, data=data)
    #status = requests.get(url)
    if response.status_code == 200:
        return "motion begin"
    else:
        return 'ErrorMessage'





#important
def telescope_RADEC_control_sync(telescope_base_url, telescope_number,RightAscension,Declination):
    '''Move the telescope to the given equatorial coordinates, return when slew is complete
    Declination coordinate (degrees)
    Right Ascension coordinate (hours)
    synchronus synchronus synchronus
    '''
    url = f"{telescope_base_url}/{str(telescope_number)}/slewtocoordinates"
    data = {'RightAscension': RightAscension,
            'Declination': Declination,
            }
    response = requests.put(url, data=data)
    #status = requests.get(url)
    if response.status_code == 200:
        return f"{'ts of post motion :'}/{telescope_time_previous_slewing_indication(telescope_base_url, telescope_number)}{' RA='}{telescope_rightAsension_value_status(telescope_base_url, telescope_number)}{' DEC='}{telescope_dec_value(telescope_base_url, telescope_number)}"
    else:
        return 'ErrorMessage'



#important
def telescope_RADEC_control_control_ASYNchronize(telescope_base_url, telescope_number,RightAscension,Declination):
        '''Move the telescope to the given equatorial coordinates, return when slew is complete
        Declination coordinate (degrees)
        Right Ascension coordinate (hours)
        unsynchronus unsynchronus unsynchronus'''


        url = f"{telescope_base_url}/{str(telescope_number)}/slewtocoordinatesasync"
        data = {'RightAscension': RightAscension,
                'Declination': Declination,
                }
        response = requests.put(url, data=data)
        #status = requests.get(url)
        if response.status_code == 200:
            return "motion begin"
        else:
            return 'ErrorMessage'






def telescope_slewtotarget_control_sync(telescope_base_url, telescope_number,RightAscension,Declination):
    '''Move the telescope to the given equatorial coordinates, return when slew is complete
    Declination coordinate (degrees)
    Right Ascension coordinate (hours)
    synchronus synchronus synchronus
    '''
    url = f"{telescope_base_url}/{str(telescope_number)}/slewtotarget"
    data = {'RightAscension': RightAscension,
            'Declination': Declination,
            }
    response = requests.put(url, data=data)
    #status = requests.get(url)
    if response.status_code == 200:
        return f"{'ts of post motion :'}/{telescope_time_previous_slewing_indication(telescope_base_url, telescope_number)}{' RA='}{telescope_rightAsension_value_status(telescope_base_url, telescope_number)}{' DEC='}{telescope_dec_value(telescope_base_url, telescope_number)}"
    else:
        return 'ErrorMessage'




def telescope_ALTAzuth_control_local_horizontal_coordinate_SYNchronize(telescope_base_url, telescope_number,Azimuth,Altitude):
    '''Matches the scope's local horizontal coordinates to the given local horizontal coordinates.'''
    url = f"{telescope_base_url}/{str(telescope_number)}/synctoaltaz"
    data = {'Azimuth': Azimuth,
            'Altitude': Altitude,
            }
    response = requests.put(url, data=data)
    if response.status_code == 200:
        return "motion begin synchronus"
    else:
        return 'ErrorMessage'



def telescope_synToCoordnate_control_sync(telescope_base_url, telescope_number,RightAscension,Declination):
    '''Matches the scope's equatorial coordinates to the given equatorial coordinates.'''

    url = f"{telescope_base_url}/{str(telescope_number)}/synctocoordinates"
    data = {'RightAscension': RightAscension,
            'Declination': Declination,
            }
    response = requests.put(url, data=data)
    #status = requests.get(url)
    if response.status_code == 200:
        return 'go to given RA DEC'
    else:
        return 'ErrorMessage'





def telescope_is_traking_indication(telescope_base_url, telescope_number):
    '''Returns the state of the telescope's sidereal tracking drive.whether the telescope is tracking'''
    url= f"{telescope_base_url}/{str(telescope_number)}/tracking?"
    return requests.get(url).json()['Value']




def telescope_traking_control(telescope_base_url, telescope_number, flag):
    '''Sets the state of the telescope's sidereal tracking drive.'''
    url = f"{telescope_base_url}/{str(telescope_number)}/tracking"
    data = {'Tracking': str(flag)}
    response = requests.put(url, data=data)
    if response.status_code == 200:
        return f"{'telescope traking'}: {flag}"
    else:
        return response.json()['ErrorMessage']



def telescope_tracking_rate_indication(telescope_base_url, telescope_number):
    '''The current tracking rate of the telescope's sidereal drive.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/trackingrate?"
    return requests.get(url).json()['Value']

def telescope_traking_rate_control(telescope_base_url, telescope_number, TrackingRate):
    '''Sets the tracking rate of the telescope's sidereal drive. 0 = driveSidereal, 1 = driveLunar, 2 = driveSolar, 3 = driveKing
     The valid range is: 0 (DriveSidereal) to 3 (DriveKing)'''
    url = f"{telescope_base_url}/{str(telescope_number)}/trackingrate"
    data = {'TrackingRate': TrackingRate}
    response = requests.put(url, data=data)
    if  3>= TrackingRate >=0 :
        if response.status_code == 200:
            return f"{'telescope traking rate'}: {TrackingRate}"
        else:
            return response.json()['ErrorMessage']
    else:
        return 'The valid range is: 0 (DriveSidereal) to 3 (DriveKing)'


def telescope_supported_DriveRates_indication(telescope_base_url, telescope_number):
    '''Returns an array of supported DriveRates values that describe the permissible values of the TrackingRate property for this telescope type.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/trackingrates?"
    return requests.get(url).json()['Value']




def telescope_telescope_internal_UTC_clock_indication(telescope_base_url, telescope_number):
    '''The UTC date/time of the telescope's internal clock in ISO 8601 format including fractional seconds. The general format (in Microsoft custom date format style) is yyyy-MM-ddTHH:mm:ss.fffffffZ E.g. 2016-03-04T17:45:31.1234567Z or 2016-11-14T07:03:08.1234567Z Please note the compulsory trailing Z indicating the 'Zulu', UTC time zone.'''
    url= f"{telescope_base_url}/{str(telescope_number)}/utcdate?"
    return requests.get(url).json()['Value']


def telescope_change_internal_UTC_clock_indication(telescope_base_url, telescope_number, telescope_utc_time):
    '''The UTC date/time of the telescope's internal clock in ISO 8601 format including fractional seconds. The general format (in Microsoft custom date format style) is yyyy-MM-ddTHH:mm:ss.fffffffZ E.g. 2016-03-04T17:45:31.1234567Z or 2016-11-14T07:03:08.1234567Z Please note the compulsory trailing Z indicating the 'Zulu', UTC time zone.'''
    url = f"{telescope_base_url}/{str(telescope_number)}/utcdate"
    data = {'UTCDate': telescope_utc_time}
    response = requests.put(url, data=data)
    if response.status_code == 200:
        return f"{'telescope datetime change'}"
    else:
        return response.json()['ErrorMessage']




def telescope_unpark_mount_control(telescope_base_url, telescope_number):
    '''Takes telescope out of the Parked state.'''
    url = f"{telescope_base_url}/{str(telescope_number)}/unpark"
    response = requests.put(url)
    if response.status_code == 200:
        return 'Telescope is now unpark'

#actions
#commandblind transmit string and dont wait for respond
#commandboolian transmit bollan to device
#commandstring transmit string to device
#['AssemblyVersionNumber', 'SlewToHA', 'AvailableTimeInThisPointingState', 'TimeUntilPointingStateCanChange']supported actions
def actions(telescope_base_url, telescope_number,Action):
    '''Actions and SupportedActions are a standardised means for drivers to extend functionality beyond the built-in capabilities of the ASCOM device interfaces.

   The key advantage of using Actions is that drivers can expose any device specific functionality required. The downside is that, in order to use these unique features, every application author would need to create bespoke code to present or exploit them.

   The Action parameter and return strings are deceptively simple, but can support transmission of arbitrarily complex data structures, for example through JSON encoding.

   This capability will be of primary value to

   * bespoke software and hardware configurations where a single entity controls both the consuming application software and the hardware / driver environment
   * a group of application and device authors to quickly formulate and try out new interface capabilities without requiring an immediate change to the ASCOM device interface, which will take a lot longer than just agreeing a name, input parameters and a standard response for an Action command.

   The list of Action commands supported by a driver can be discovered through the SupportedActions property.

   This method should return an error message and NotImplementedException error number (0x400) if the driver just implements the standard ASCOM device methods and has no bespoke, unique, functionality'''


    url = f"{telescope_base_url}/{str(telescope_number)}/action"
    data={
        'Action':Action
    }
    response = requests.put(url,data)
    if response.status_code==200:
        return 'action is supported'
    else:
        return 'Not supported'




