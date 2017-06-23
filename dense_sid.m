function dense_sid(image_files, output_file, central_fraction, stride)
settings.sc_min = 3;        %% min ring radius
settings.sc_max = 50;      %% max ring radius
settings.nsteps = 10;       %% number of rings
settings.nrays  = 16;       %% number of rays
settings.sc_sig = 0.1400;   %% (Gaussian sigma / ring radius) ratio
settings.nors   = 4;        %% number of derivative orientations
settings.cmp    = 0;        %% compress the invariant descriptor

num_files = length(image_files);

features = cell(1, num_files);

for i = 1:num_files
    image = imread(image_files{i});
    
    if and(~isempty(central_fraction), central_fraction ~= 1.0)
        shape = size(image);
        fraction_offset = floor(1 / ((1 - central_fraction) / 2.0));

        bbox_h_start = floor(shape(1) / fraction_offset);
        bbox_w_start = floor(shape(2) / fraction_offset);

        bbox_h_stop = (shape(1) - bbox_h_start);
        bbox_w_stop = (shape(2) - bbox_w_start);

        image = image(bbox_h_start+1:bbox_h_stop,bbox_w_start+1:bbox_w_stop);
    end
    
    [~, invar] = get_descriptors(image, settings, stride);
    features{i} = invar;
end

save(output_file, 'features') 

end
