#!/usr/bin/python3

def main():
    from ak09915 import AK09915
    from llog import LLogWriter

    device = "ak09915"
    parser = LLogWriter.create_default_parser(__file__, device)
    args = parser.parse_args()


    with LLogWriter(args.meta, args.output, console=args.console) as log:
        ak = AK09915()

        def data_getter():
            data = ak.measure()
            return f"{data.x_raw} {data.y_raw} {data.z_raw} {data.x:.6f} {data.y:.6f} {data.z:.6f}"

        log.log_data_loop(data_getter, parser_args=args)

if __name__ == '__main__':
    main()
