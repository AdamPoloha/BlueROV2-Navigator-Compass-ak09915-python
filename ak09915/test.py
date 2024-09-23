#!/usr/bin/python3

def main():
    from ak09915 import AK09915

    device = "ak09915"

    ak = AK09915()

    def data_getter():
        data = ak.measure()
        #print(f"{data.x_raw} {data.y_raw} {data.z_raw} {data.x:.6f} {data.y:.6f} {data.z:.6f}")
        print(data.x_raw,data.y_raw,data.z_raw,data.x,data.y,data.z)

    while True:
        data_getter()

if __name__ == '__main__':
    main()
