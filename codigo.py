 ds = gdal.Open(in_path + input_filename)
    band = ds.GetRasterBand(1)
    xsize = band.XSize
    ysize = band.YSize
    tile_size_x = 256
    tile_size_y = 256
    for i in range(0, xsize, tile_size_x):
        for j in range(0, ysize, tile_size_y):
            indice = indice + 1 
                      
            com_string = "gdal_translate -of GTIFF -srcwin " + str(i)+ ", " + str(j) + ", " + str(tile_size_x) + ", " + str(tile_size_y) + " " + str(in_path) + str(input_filename) + " " + str(directorio) + str("train_")+str(indice)  + ".tif"
            os.system(com_string)
    return indice;