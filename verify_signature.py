import cv2
import numpy as np

# Load the reference signature image
ref_image = cv2.imread('011011_004.png', cv2.IMREAD_GRAYSCALE)

# Load the test signature image
test_image = cv2.imread('021005_002.png', cv2.IMREAD_GRAYSCALE)

# Resize the images to a common size
ref_image = cv2.resize(ref_image, (test_image.shape[1], test_image.shape[0]))

# Initialize the SIFT detector and matcher
sift = cv2.SIFT_create()
bf = cv2.BFMatcher()

# Detect and compute the keypoints and descriptors for the reference and test images
ref_keypoints, ref_descriptors = sift.detectAndCompute(ref_image, None)
test_keypoints, test_descriptors = sift.detectAndCompute(test_image, None)

# Match the descriptors using the Brute-Force matcher
matches = bf.knnMatch(ref_descriptors, test_descriptors, k=2)

# Apply ratio test to filter matches
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# Calculate the similarity score
similarity_score = len(good_matches) / len(ref_keypoints) * 100

# Print the similarity score
print(f'Similarity score: {similarity_score:.2f}%')

# Check if the signature is fraudulent
if similarity_score < 80:
    print('The signature is likely fraudulent.')
else:
    print('The signature is likely genuine.')