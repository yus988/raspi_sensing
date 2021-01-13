import spidev
import time
from time import perf_counter
import csv
import datetime
import ADXL362



def main():

    # 書き込むファイルの作成
    dt_now = datetime.datetime.now()
    filename = './csv/' + dt_now.strftime('%m-%d_%H-%M-%S') + '.csv'
    print(dt_now.strftime('%m%d_%H-%M-%S'))

    # ファイルオープン
    f = open(filename, 'w')
    writer = csv.writer(f, lineterminator='\n')
    csvlist = []

    # #初期設定
    # spi = spidev.SpiDev()   
    # spi.open(0,0)
    # spi.mode = 3  #ADXL345このデバイスはSPI mode3で動作
    # spi.max_speed_hz = 1000000
    
    # spi.xfer2([0x2D, 0x02]) #測定スタート

    # #初期設定
    # spi2 = spidev.SpiDev()   
    # spi2.open(0,1)
    # spi2.mode = 3  #ADXL345このデバイスはSPI mode3で動作
    # spi2.max_speed_hz = 1000000
    
    # spi2.xfer2([0x2D, 0x02]) #測定スタート

    accel_0 = ADXL362.ADXL362(0, 0)
    accel_0.begin_measure()
    accel_1 = ADXL362.ADXL362(0,1)
    accel_1.begin_measure()

    try:
        while True:
            #x,y,z方向の加速度を取得(2の補数表現)

            # x_data_list = spi.xfer2([0xc0|0x32, 0x00, 0x00])
            # y_data_list = spi.xfer2([0xc0|0x34, 0x00, 0x00])
            # z_data_list = spi.xfer2([0xc0|0x36, 0x00, 0x00])
            # x_data = x_data_list[1] | (x_data_list[2] << 8)
            # y_data = y_data_list[1] | (y_data_list[2] << 8)
            # z_data = z_data_list[1] | (z_data_list[2] << 8)
            # #2の補数を10進に変換
            # if(x_data & 0x8000):
            #     x_data = ((~x_data & 0xFFFF) + 1)*-1
            # if(y_data & 0x8000):    
            #     y_data = ((~y_data & 0xFFFF) + 1)*-1
            # if(z_data & 0x8000):
            #     z_data = ((~z_data & 0xFFFF) + 1)*-1
            # #加速度に変換（Dレンジ ±2g）
            # x_data = 2 * 9.8 * x_data / 0x7FFF
            # y_data = 2 * 9.8 * y_data / 0x7FFF
            # z_data = 2 * 9.8 * z_data / 0x7FFF

            # csvlist.append([perf_counter(),x_data,y_data,z_data,"#1"])

            # print(perf_counter(),"#1")
            # print('x: {:4.2f}, y: {:4.2f}, z: {:4.2f} [m/s^2]'.format(x_data, y_data, z_data))
            # time.sleep(0.1)

            # #x,y,z方向の加速度を取得(2の補数表現)
            # x_data_list = spi2.xfer2([0xc0|0x32, 0x00, 0x00])
            # y_data_list = spi2.xfer2([0xc0|0x34, 0x00, 0x00])
            # z_data_list = spi2.xfer2([0xc0|0x36, 0x00, 0x00])
            # x_data = x_data_list[1] | (x_data_list[2] << 8)
            # y_data = y_data_list[1] | (y_data_list[2] << 8)
            # z_data = z_data_list[1] | (z_data_list[2] << 8)

            x_data  =  accel_1.read_xyz()[0]
            y_data  =  accel_1.read_xyz()[1]
            z_data  =  accel_1.read_xyz()[2]

            #2の補数を10進に変c換
        
            if(x_data & 0x8000):
                x_data = ((~x_data & 0xFFFF) + 1)*-1
            if(y_data & 0x8000):    
                y_data = ((~y_data & 0xFFFF) + 1)*-1
            if(z_data & 0x8000):
                z_data = ((~z_data & 0xFFFF) + 1)*-1
            #加速度に変換（Dレンジ ±2g）
            x_data = 2 * 9.8 * x_data / 0x7FFF
            y_data = 2 * 9.8 * y_data / 0x7FFF
            z_data = 2 * 9.8 * z_data / 0x7FFF

            csvlist.append([perf_counter(),x_data,y_data,z_data,"#2"])

            print(perf_counter(),"#2")
            print('x: {:4.2f}, y: {:4.2f}, z: {:4.2f} [m/s^2]'.format(x_data, y_data, z_data))
            # time.sleep(0.1)

        
    except KeyboardInterrupt:
        writer.writerows(csvlist)
        f.close()
        print('!FINISH!')
    
if __name__ == "__main__":
    main()
