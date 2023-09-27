# modify to your data path
input_path=/app/data/blend_labeled
# modify the width and height according to your data
W=640
H=640

# import the repo paths
source /repos/LMI_AI_Solutions/lmi_ai.env

# resize images with labels
python -m label_utils.resize_with_csv --path_imgs $input_path --out_imsz $W,$H --path_out /app/data/resized

# convert to yolo format
# remote the --seg flag if you want to train a object detection model
python -m label_utils.convert_data_to_yolo --path_imgs /app/data/resized --path_out /app/data/resized_yolo
