; This puts the paths for the IDL astronomy library, acis extract, and
; TARA into the IDL !path variable

PRO set_dirs

dir1 = '/scratch/rumbaugh'
dir2 = '/scratch/rumbaugh/ae'
dir3 = '/scratch/rumbaugh/tara'
dir4 = '/scratch/rumbaugh/tara/acis'
dir5 = '/scratch/rumbaugh/tara/event_browser'
dir6 = '/scratch/rumbaugh/tara/utilities'
dir7 = '/scratch/rumbaugh/tara/widget_tools'
dir8 = '/scratch/rumbaugh/IDLAstroLib/pro/astro'
dir9 = '/scratch/rumbaugh/IDLAstroLib/pro/astrom'
dir10 = '/scratch/rumbaugh/IDLAstroLib/pro/database'
dir11 = '/scratch/rumbaugh/IDLAstroLib/pro/disk_io'
dir12 = '/scratch/rumbaugh/IDLAstroLib/pro/fits'
dir13 = '/scratch/rumbaugh/IDLAstroLib/pro/fits_bintable'
dir14 = '/scratch/rumbaugh/IDLAstroLib/pro/fits_table'
dir15 = '/scratch/rumbaugh/IDLAstroLib/pro/idlphot'
dir16 = '/scratch/rumbaugh/IDLAstroLib/pro/image'
dir17 = '/scratch/rumbaugh/IDLAstroLib/pro/jhuapl'
dir18 = '/scratch/rumbaugh/IDLAstroLib/pro/math'
dir19 = '/scratch/rumbaugh/IDLAstroLib/pro/misc'
dir20 = '/scratch/rumbaugh/IDLAstroLib/pro/plot'
dir21 = '/scratch/rumbaugh/IDLAstroLib/pro/robust'
dir22 = '/scratch/rumbaugh/IDLAstroLib/pro/sdas'
dir23 = '/scratch/rumbaugh/IDLAstroLib/pro/sdas_table'
dir24 = '/scratch/rumbaugh/IDLAstroLib/pro/sockets'
dir25 = '/scratch/rumbaugh/IDLAstroLib/pro/structure'
dir26 = '/scratch/rumbaugh/IDLAstroLib/pro/tv'
dir27 = '/scratch/rumbaugh/ciaotesting'
dir28 = '/scratch/rumbaugh/marx-dist-4.4.0'
dir29 = '/scratch/rumbaugh/marx-dist-4.4.0/marx'
dir30 = '/scratch/rumbaugh/marx-dist-4.4.0/marx/src'
dir31 = '/scratch/rumbaugh/marx-dist-4.4.0/jdfits/src'
dir32 = '/scratch/rumbaugh/marx-dist-4.4.0/jdmath/src'
dir33 = '/scratch/rumbaugh/marx-dist-4.4.0/marx/bin'
dir34 = '/scratch/rumbaugh/marx-dist-4.4.0/marx/lib'
dir35 = '/scratch/rumbaugh/marx-dist-4.4.0/marx/libsrc'
dir36 = '/scratch/rumbaugh/marx-dist-4.4.0/marx/src/objs'
dir37 = '/scratch/rumbaugh/Chandra_ORELSE_Notes'
dir38 = '/scratch/rumbaugh/coyote'
dir39 = '/scratch/rumbaugh/runs'
dir40 = '/home/rumbaugh/forNick'

!Path = dir1 + ":" + dir2 + ":" + dir3 + ":" + dir4 + ":" + dir5 + ":" + dir6 + ":" + dir7 + ":" + dir8 + ":" + dir9 + ":" + dir10 + ":" + dir11 + ":" + dir12 + ":" + dir13 + ":" + dir14 + ":" + dir15 + ":" + dir16 + ":" + dir17 + ":" + dir18 + ":" + dir19 + ":" + dir20 + ":" + dir21 + ":" + dir22 + ":" + dir23 + ":" + dir24 + ":" + dir25 + ":" + dir26 + ":" + dir27 + ":" + dir28 + ':' + dir29  + ':' + dir30 + ':' + dir31 + ':' + dir32 + ':' + dir33 + ':' + dir34 + ':' + dir35 + ':' + dir36 + ":" + dir37 + ":" + dir38 + ":" + dir39 + ":" + dir40 + ":" + !Path

end
