# No longer maintained as I have moved to using [Home Assistant](https://www.home-assistant.io/).


![Build Status](https://github.com/colin-nolan/ansible-shinobi/actions/workflows/main.yml/badge.svg)

# Ansible Shinobi
_Ansible role and modules for installing and configuring a 
[Dockerised installation](https://github.com/colin-nolan/docker-shinobi) of 
[Shinobi](https://gitlab.com/Shinobi-Systems/Shinobi) (an open-source video management solution)._


## Requirements
- Debian/Ubuntu (un-tested for other distributions).
- x86, armv7 or aarch64 architectures (i.e. works on Raspberry Pi 2+).
- Docker on the host machine.
- [`shinobi-client` Python package](](https://github.com/colin-nolan/python-shinobi)).


## Usage
### Role
#### Installation
[Install from Ansible Galaxy](https://galaxy.ansible.com/colin_nolan/shinobi):
```bash
ansible-galaxy install colin_nolan.shinobi
```
The [shinobi_user](library/shinobi_user.py) and [shinobi_monitor](library/shinobi_monitor.py) modules used by this 
library require the Python package `shinobi-client` to be installed on the machine running the role:
`pip install shinobi-client`

#### Configuration
For configuration options, please [see the defaults file](defaults/main.yml). Note that there are a number of
configuration values that must be provided (detailed provided at the top of the defaults file, linked above).

Important notes:
- The default Shinobi installation (non-community edition) is not free for use in all situations - see `shinobi_source`.
- The default Shinobi Docker base image has a build of `ffmpeg` (the software that deals with video) that is will not be
  optimised for your host - see `shinobi_docker_shinobi_base_image`.

#### Example:
```yaml
# playbook.yml

- hosts: shinobi-servers
  roles:
     - colin_nolan.shinboi
  vars:
    shinobi_database_root_password: password123
    shinobi_database_user_name: user123
    shinobi_database_user_password: password123

    shinobi_super_user_email: admin@localhost
    shinobi_super_user_password: password123
    shinobi_super_user_token: token123

    shinobi_host_address: 0.0.0.0
    shinobi_host_port: 8080

    shinobi_source:
      repository: https://gitlab.com/Shinobi-Systems/Shinobi.git
      branch: master

    shinobi_docker_shinobi_base_image: colinnolan/ffmpeg:latest

    shinobi_users:
      - email: user@localhost
        password: password123
      - email: user2@localhost
        password: password456
      - email: user3@localhost
        password: password789

    shinobi_monitors:
      - id: example_1
        users:
          - user@localhost
          - user2@localhost
        # If you setup a monitor in shinobi, you can then export
        # it to get the configuration (which will look like the below)
        configuration:
          name: example_1
          type: h264
          protocol: rtsp
          host: 192.168.0.1
          port: 554
          path: /h264Preview_01_main
          height: 480
          width: 640
          ext: mp4
          fps: 1
          details: "{\"max_keep_days\":\"\",\"notes\":\"\",\"dir\":\"\",\"rtmp_key\":\"\",\"auto_host_enable\":\"0\",\"auto_host\":\"rtsp://user:pass@192.168.0.1:554/h264Preview_01_main\",\"rtsp_transport\":\"tcp\",\"muser\":\"user\",\"mpass\":\"pass\",\"port_force\":\"0\",\"fatal_max\":\"0\",\"skip_ping\":\"0\",\"is_onvif\":\"1\",\"onvif_port\":\"\",\"primary_input\":null,\"aduration\":\"1000000\",\"probesize\":\"1000000\",\"stream_loop\":\"0\",\"sfps\":\"25\",\"accelerator\":\"1\",\"hwaccel\":\"auto\",\"hwaccel_vcodec\":\"\",\"hwaccel_device\":\"\",\"use_coprocessor\":\"1\",\"stream_type\":\"hls\",\"stream_flv_type\":\"ws\",\"stream_flv_maxLatency\":\"\",\"stream_mjpeg_clients\":\"\",\"stream_vcodec\":\"copy\",\"stream_acodec\":\"\",\"hls_time\":\"2\",\"hls_list_size\":\"3\",\"preset_stream\":\"ultrafast\",\"signal_check\":\"10\",\"signal_check_log\":\"0\",\"stream_quality\":\"15\",\"stream_fps\":\"2\",\"stream_scale_x\":\"\",\"stream_scale_y\":\"\",\"rotate_stream\":\"no\",\"svf\":\"\",\"tv_channel\":\"0\",\"tv_channel_id\":\"\",\"tv_channel_group_title\":\"\",\"stream_timestamp\":\"0\",\"stream_timestamp_font\":\"\",\"stream_timestamp_font_size\":\"\",\"stream_timestamp_color\":\"\",\"stream_timestamp_box_color\":\"\",\"stream_timestamp_x\":\"\",\"stream_timestamp_y\":\"\",\"stream_watermark\":\"0\",\"stream_watermark_location\":\"\",\"stream_watermark_position\":\"tr\",\"snap\":\"0\",\"snap_fps\":\"\",\"snap_scale_x\":\"\",\"snap_scale_y\":\"\",\"snap_vf\":\"\",\"vcodec\":\"copy\",\"crf\":\"1\",\"acodec\":\"no\",\"record_scale_y\":\"\",\"record_scale_x\":\"\",\"cutoff\":\"15\",\"rotate_record\":\"no\",\"vf\":\"\",\"timestamp\":\"0\",\"timestamp_font\":\"\",\"timestamp_font_size\":\"10\",\"timestamp_color\":\"white\",\"timestamp_box_color\":\"0x00000000@1\",\"timestamp_x\":\"(w-tw)/2\",\"timestamp_y\":\"0\",\"watermark\":\"0\",\"watermark_location\":\"\",\"watermark_position\":\"tr\",\"record_timelapse\":null,\"record_timelapse_mp4\":null,\"record_timelapse_fps\":null,\"record_timelapse_scale_x\":\"\",\"record_timelapse_scale_y\":\"\",\"record_timelapse_vf\":\"\",\"record_timelapse_watermark\":null,\"record_timelapse_watermark_location\":\"\",\"record_timelapse_watermark_position\":null,\"cust_input\":\"\",\"cust_stream\":\"\",\"cust_snap\":\"\",\"cust_record\":\"\",\"cust_detect\":\"\",\"cust_sip_record\":\"\",\"custom_output\":\"\",\"detector\":\"0\",\"detector_http_api\":null,\"detector_send_frames\":\"1\",\"detector_lock_timeout\":\"\",\"detector_save\":\"0\",\"detector_fps\":\"\",\"detector_scale_x\":\"640\",\"detector_scale_y\":\"480\",\"detector_record_method\":\"sip\",\"detector_trigger\":\"1\",\"detector_trigger_record_fps\":\"\",\"detector_timeout\":\"10\",\"detector_send_video_length\":\"\",\"watchdog_reset\":\"0\",\"detector_delete_motionless_videos\":\"0\",\"det_multi_trig\":null,\"group_detector_multi\":\"\",\"detector_webhook\":\"0\",\"detector_webhook_url\":\"\",\"detector_webhook_method\":null,\"detector_command_enable\":\"0\",\"detector_command\":\"\",\"detector_command_timeout\":\"\",\"detector_mail\":\"0\",\"detector_mail_timeout\":\"\",\"detector_discordbot\":null,\"detector_discordbot_send_video\":null,\"detector_discordbot_timeout\":\"\",\"use_detector_filters\":null,\"use_detector_filters_object\":null,\"cords\":\"[]\",\"detector_filters\":\"\",\"detector_pam\":\"1\",\"detector_show_matrix\":null,\"detector_sensitivity\":\"\",\"detector_max_sensitivity\":\"\",\"detector_threshold\":\"1\",\"detector_color_threshold\":\"\",\"detector_frame\":\"0\",\"detector_noise_filter\":null,\"detector_noise_filter_range\":\"\",\"detector_notrigger\":\"0\",\"detector_notrigger_mail\":\"0\",\"detector_notrigger_timeout\":\"\",\"detector_audio\":null,\"detector_audio_min_db\":\"\",\"detector_audio_max_db\":\"\",\"detector_use_detect_object\":\"0\",\"detector_send_frames_object\":null,\"detector_obj_region\":null,\"detector_use_motion\":\"1\",\"detector_fps_object\":\"\",\"detector_scale_x_object\":\"\",\"detector_scale_y_object\":\"\",\"detector_lisence_plate\":\"0\",\"detector_lisence_plate_country\":\"us\",\"detector_buffer_vcodec\":\"auto\",\"detector_buffer_acodec\":null,\"detector_buffer_fps\":\"\",\"detector_buffer_hls_time\":\"\",\"detector_buffer_hls_list_size\":\"\",\"detector_buffer_start_number\":\"\",\"detector_buffer_live_start_index\":\"\",\"control\":\"0\",\"control_base_url\":\"\",\"control_url_method\":null,\"control_digest_auth\":null,\"control_stop\":\"0\",\"control_url_stop_timeout\":\"\",\"control_url_center\":\"\",\"control_url_left\":\"\",\"control_url_left_stop\":\"\",\"control_url_right\":\"\",\"control_url_right_stop\":\"\",\"control_url_up\":\"\",\"control_url_up_stop\":\"\",\"control_url_down\":\"\",\"control_url_down_stop\":\"\",\"control_url_enable_nv\":\"\",\"control_url_disable_nv\":\"\",\"control_url_zoom_out\":\"\",\"control_url_zoom_out_stop\":\"\",\"control_url_zoom_in\":\"\",\"control_url_zoom_in_stop\":\"\",\"groups\":\"[]\",\"loglevel\":\"warning\",\"sqllog\":\"0\",\"detector_cascades\":\"\",\"stream_channels\":\"\",\"input_maps\":\"\",\"input_map_choices\":\"\"}"
```

### Modules
There are 2 Ansible modules in this project that you may wish to use (without necessarily using the role - put them into
your library):
- [`shinobi_user`](library/shinobi_user.py): manages users.
- [`shinobi_monitor`](library/shinobi_monitor.py): manages monitors (user camera setups).


## Development
### Requirements
- Python >= 3.6 with pip for testing.

### Testing
Testing has been setup with molecule. To install:
```bash
pip install -r molecule/default/requirements.txt
```
To run all tests:
```
module test [--destory=never]
```


## Related Projects
- [Dockerised Shinobi setup](https://github.com/colin-nolan/docker-shinobi).
- [Shinobi Pythion client](https://github.com/colin-nolan/python-shinobi).


## Alternatives
- [Official Ansible role](https://gitlab.com/Shinobi-Systems/ansible-shinobi) - not containerised, a little unpolished.


## Legal
[GPL v3.0](LICENSE.txt). Copyright 2019, 2020 Colin Nolan.

I am not affiliated to the development of Shinobi project in any way.

This work is in no way related to the company that I work for.
