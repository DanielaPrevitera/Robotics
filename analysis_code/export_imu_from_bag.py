import csv
import sys

import rosbag2_py
from rclpy.serialization import deserialize_message
from rosidl_runtime_py.utilities import get_message


def export_imu(bag_path, topic_name, output_csv):
    storage_options = rosbag2_py.StorageOptions(
        uri=bag_path,
        storage_id="sqlite3"
    )

    converter_options = rosbag2_py.ConverterOptions(
        input_serialization_format="cdr",
        output_serialization_format="cdr"
    )

    reader = rosbag2_py.SequentialReader()
    reader.open(storage_options, converter_options)

    topic_types = reader.get_all_topics_and_types()
    type_map = {topic.name: topic.type for topic in topic_types}

    if topic_name not in type_map:
        print(f"Topic {topic_name} non trovato nel bag.")
        print("Topic disponibili:")
        for name, msg_type in type_map.items():
            print(f"  {name}: {msg_type}")
        return

    msg_type = get_message(type_map[topic_name])

    with open(output_csv, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "t_rosbag_ns",
            "stamp_sec",
            "stamp_nanosec",
            "frame_id",

            "orientation_x",
            "orientation_y",
            "orientation_z",
            "orientation_w",

            "angular_velocity_x",
            "angular_velocity_y",
            "angular_velocity_z",

            "linear_acceleration_x",
            "linear_acceleration_y",
            "linear_acceleration_z"
        ])

        count = 0

        while reader.has_next():
            topic, data, t = reader.read_next()

            if topic != topic_name:
                continue

            msg = deserialize_message(data, msg_type)

            writer.writerow([
                t,
                msg.header.stamp.sec,
                msg.header.stamp.nanosec,
                msg.header.frame_id,

                msg.orientation.x,
                msg.orientation.y,
                msg.orientation.z,
                msg.orientation.w,

                msg.angular_velocity.x,
                msg.angular_velocity.y,
                msg.angular_velocity.z,

                msg.linear_acceleration.x,
                msg.linear_acceleration.y,
                msg.linear_acceleration.z
            ])

            count += 1

    print(f"Esportati {count} messaggi in {output_csv}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso:")
        print("python3 export_imu_from_bag.py <bag_path> <topic_name> <output_csv>")
        print()
        print("Esempio:")
        print("python3 export_imu_from_bag.py . /livox/imu imu.csv")
        sys.exit(1)

    bag_path = sys.argv[1]
    topic_name = sys.argv[2]
    output_csv = sys.argv[3]

    export_imu(bag_path, topic_name, output_csv)
