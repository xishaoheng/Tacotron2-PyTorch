from text import symbols


class hparams:
	seed = 0

	################################
	# Data Parameters              #
	################################
	text_cleaners=['english_cleaners']

	################################
	# Audio                        #
	################################
	num_mels = 80
	num_freq = 513
	sample_rate = 16000
	frame_shift = 160
	frame_length = 1024
	preemphasis = 0.97
	min_level_db = -100
	ref_level_db = 20
	fmin = 0
	fmax = 8000
	power = 1.5
	gl_iters = 30

	################################
	# Train                        #
	################################
	is_cuda = True
	pin_mem = True
	n_workers = 1
	prep = False
	pth = ''
	lr = 2e-3
	betas = (0.9, 0.999)
	eps = 1e-6
	sch = True
	sch_step = 4000
	max_iter = 200e3
	batch_size = 16
	iters_per_log = 10
	iters_per_sample = 200
	iters_per_ckpt = 2000
	weight_decay = 1e-6
	grad_clip_thresh = 1.0
	mask_padding = True
	p = 10 # mel spec loss penalty
	eg_text = 'Make America great again!'

	################################
	# Model Parameters             #
	################################
	n_symbols = len(symbols)
	symbols_embedding_dim = 512

	# Encoder parameters
	encoder_kernel_size = 5
	encoder_n_convolutions = 3
	encoder_embedding_dim = 512

	# Decoder parameters
	n_frames_per_step = 3
	decoder_rnn_dim = 1024
	prenet_dim = 256
	max_decoder_steps = 1000
	gate_threshold = 0.5
	p_attention_dropout = 0.1
	p_decoder_dropout = 0.1

	# Attention parameters
	attention_rnn_dim = 1024
	attention_dim = 256

	# Location Layer parameters
	attention_location_n_filters = 32
	attention_location_kernel_size = 31

	# Mel-post processing network parameters
	postnet_embedding_dim = 512
	postnet_kernel_size = 5
	postnet_n_convolutions = 5

