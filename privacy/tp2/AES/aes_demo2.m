%	AES_DEMO2  Demonstration of AES-components using an image
%
%   AES_DEMO2
%   runs a demonstration of all components of 
%   the Advanced Encryption Standard (AES) toolbox.
%
%   In the initialization step the S-boxes, the round constants,
%   and the polynomial matrices are created and
%   an example cipher key is expanded into 
%   the round key schedule.
%   Step two and three finally convert 
%   an example plaintext to ciphertext and back to plaintext.
%   Copyright 2001-2005, J. J. Buchholz, Hochschule Bremen, buchholz@hs-bremen.de
%   Version 1.0     30.05.2001


function aes_demo2;

close all;

% AES cipher Initialization
[s_box, inv_s_box, w, poly_mat, inv_poly_mat] = aes_init;

% Read in an image as UINT8_t
im = imread('cameraman.tif');

% Resize the image to [64 64] to speed up the calculation and cast to matlab double
im = double(imresize(im, [64 64]));

% Show result on screen in a new figure
figure;imshow(im, []); title('resized original image');

% AES operates on 16 byte blocks at the time. The image does gets sliced into [4 4] blocks
% which are packed in a matlab cell datastructure
blk_size 	= 4;
pattern 	= repmat(blk_size, [1 64/blk_size]);
im_cell_c 	= mat2cell(im, pattern, pattern);

% Loop over all [4 4] cells and encrypt the contents
for i = 1:1:size(im_cell_c, 1)
	for j = 1:1:size(im_cell_c, 2)			
		im_cell_c{i, j} = reshape(cipher(im_cell_c{i,j}(:), w, s_box, poly_mat), [4 4]);
	end
end

% Build an image from the cell data structure
im_c = cell2mat(im_cell_c);

% Show result on screen in a new figure
figure;imshow(im_c, []);title('encryption')


%--------------------------------------------------------------------------
%	MODEL BLOCK LOSS HERE
%
%
%
%--------------------------------------------------------------------------


im_cell_c = mat2cell(im_c, pattern, pattern);

% Reserve space for a new cell with 16x16 blocks, each who will contain a 16 byte matrix
% shaped as [4 4]
replain_cell = cell(16, 16);

% Get the 16 bytes from each cell individually and decrypt them.
k = 1;
for i = 1:1:size(im_cell_c, 1)
	for j = 1:1:size(im_cell_c, 2)			
		replain_cell{i, j} = reshape(inv_cipher(im_cell_c{i, j}(:), w, inv_s_box, inv_poly_mat), [4 4]);
        k = k+1;
	end
end

% Remap the cell structure to a normale image
re_plain = cell2mat(replain_cell);


% Show result on screen in a new figure
figure;imshow(re_plain, []); title('decrypted image');

