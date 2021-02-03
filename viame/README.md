# To run these in VIAME Annotation GUI
1. Copy files inside 2021_pipelines/embedded_single_stream to your viame/build/install/configs/pipelines/embedded_single_stream
2. Copy folder 2021_pipelines/common into your viame/build/istall/configs/pipelines/ 
3. Copy folder 2021_models/ into your viame/build/install/configs folder

Now when you launch the annotation interface these pipelines should appear under Tools > Execute Pipeline

# To run the ir->eo subregion trigger in sealtk GUI
1. Copy files inside 2021_pipelines/embedded_dual_stream to your sealtk/build/install/configs/pipelines/embedded_dual_stream
2. Copy folder 2021_pipelines/common into your viame/build/install/configs/pipelines/ 
3. Copy folder 2021_models/ into your viame/build/install/configs folder


# To run these pipelines via command line shell
1. Clone this repo
2. Copy the viame directory into your viame/build/install/examples/ folder
3. Rename the directory from viame to something that makes more sense such in that context such as seal_object_detection
You should now have a seal_object_detection folder in your the examples folder
4. Inside this seal_object_detection folder there are .sh files corresponding to different pipelines.  To run these you type 'bash what_i_want_to_run.sh'
