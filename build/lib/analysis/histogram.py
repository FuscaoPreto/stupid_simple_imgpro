def histogram(img_path):
    # Load the image using numpy
    img = plt.imread(img_path)

    # Convert the image to grayscale if it's a color image
    if len(img.shape) > 2:
        img = np.mean(img, axis=2)

    # Flatten the image array
    img_flat = img.flatten()

    # Calculate the histogram using numpy
    histogram_values, bins = np.histogram(img_flat, bins=256, range=(0, 256))

    # Create x-axis values from 0 to 255
    x = np.arange(256)

    # Plot the histogram
    plt.bar(x, histogram_values)

    # Set the x-axis and y-axis labels
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')

    # Show the histogram
    plt.show()

    # Return the histogram values
    return histogram_values
