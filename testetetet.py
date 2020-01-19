

// Load main image
Mat bgr_frame = imread("glare.png");

if (bgr_frame.empty())
{
    cout << "Error loading image file" << endl;
    return -1;
}

// Convert from BGR to HSV
Mat hsv_frame;
cvtColor(bgr_frame, hsv_frame, CV_BGR2HSV);

// Split HSV into H, S, V channels
Mat channels[3];
split(hsv_frame, channels);

// Get mask
threshold(channels[0], channels[0], 63, 255, CV_THRESH_BINARY);

// Use mask to generate a BGR image
Mat output(channels[0].rows, channels[0].cols, CV_8UC3);

for (int j = 0; j < channels[0].rows; j++)
{
    for (int i = 0; i < channels[0].cols; i++)
    {
        unsigned char val = channels[0].at<unsigned char>(j, i);

        if (255 == val)
        {
            output.at<Vec3b>(j, i)[0] = 189;
            output.at<Vec3b>(j, i)[1] = 108;
            output.at<Vec3b>(j, i)[2] = 47;
        }
        else
        {
            output.at<Vec3b>(j, i)[0] = 94;
            output.at<Vec3b>(j, i)[1] = 206;
            output.at<Vec3b>(j, i)[2] = 236;
        }
    }
}

imshow("hue", channels[0]);
imshow("output", output);
waitKey();