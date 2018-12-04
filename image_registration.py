# Created by Qixun Qu
# quqixun@gmail.com
# 2017/04/10
#


import numpy as np
from affine_ransac import Ransac
from align_transform import Align
from affine_transform import Affine

# Affine Transform
# |x'|  = |a, b| * |x|  +  |tx|
# |y'|    |c, d|   |y|     |ty|
# pts_t =    A   * pts_s  + t

# -------------------------------------------------------------
# Test Class Affine
# -------------------------------------------------------------

# Create instance
af = Affine()

# Generate a test case as validation with
# a rate of outliers
outlier_rate = 0.9
A_true, t_true, pts_s, pts_t = af.create_test_case(outlier_rate)

# At least 3 corresponding points to
# estimate affine transformation
K = 3
# Randomly select 3 pairs of points to do estimation
idx = np.random.randint(0, pts_s.shape[1], (K, 1))
A_test, t_test = af.estimate_affine(pts_s[:, idx], pts_t[:, idx])

# Display known parameters with estimations
# They should be same when outlier_rate equals to 0,
# otherwise, they are totally different in some cases
print(A_true, '\n', t_true)
print(A_test, '\n', t_test)

# -------------------------------------------------------------
# Test Class Ransac
# -------------------------------------------------------------

# Create instance
rs = Ransac(K=3, threshold=1)

residual = rs.residual_lengths(A_test, t_test, pts_s, pts_t)

# Run RANSAC to estimate affine tansformation when
# too many outliers in points set
A_rsc, t_rsc, inliers = rs.ransac_fit(pts_s, pts_t)
print(A_rsc, '\n', t_rsc)

# -------------------------------------------------------------
# Test Class Align
# -------------------------------------------------------------

# Load source image and target image
source_path = 'Images/27_vis.bmp'
target_path = 'Images/27_nir.bmp'

# Create instance
al = Align(source_path, target_path, threshold=1)

# Image transformation
merge, M = al.align_image()

####demo####
nir_key = [342.08, 192.6, 391.09, 187.9, 358.27,
           219.42, 343.53, 248.59, 390.88, 248.09]
box = [322, 132, 322 + 112, 132 + 144]
al.show_with_points(M, nir_key, box)
print 'o'
