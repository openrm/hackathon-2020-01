.SILENT: run

run:
	# Download trained weights to `output/model.h5`, etc.
	docker run -i $(shell docker build -q .) \
		--model_path output/model.h5 \
		--image_dir data/test \
		2> /dev/null
