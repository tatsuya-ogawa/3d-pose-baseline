import tfcoreml as tf_converter

tf_converter.convert(tf_model_path = 'pb/graph.pb',
                     mlmodel_path = '3d-pose-baselne.mlmodel',
                     output_feature_names = ['linear_model/add_1:0'],
                     input_name_shape_dict = {
			'inputs/enc_in:0':[1,32]
		     })
