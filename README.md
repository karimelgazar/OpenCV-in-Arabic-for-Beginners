<p align="center"> 
<img src="images/allah.png" height=500 width=500/>
</p>

# OpenCV In Arabic For Beginners

## About The Course
### This course is for beginners in Computer Vision or OpenCV
### Click the image below to go to the course playlist on Youtube

<a href="https://www.youtube.com/playlist?list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z" target="_blank"><img src="images/cover.png"></a>
---

## Setup

To run the code, you need the packages ``numpy``, ``scipy``, ``scikit-learn``, ``matplotlib``, ``scikit-image``, ``mahotas`` and ``opencv-python``.

The easiest way to set up an environment is by installing [Anaconda](https://www.anaconda.com/distribution/).

### Make sure that you added anconda to your system variable
So you can use it in any directory on your PC

    -------> User Variables <------- 
    Installation_Path\Anaconda\python.exe
    Installation_Path\Anaconda\Scripts
    Installation_Path\Anaconda\Library\bin
    Installation_Path\Anaconda\Library\usr\bin
    Installation_Path\Anaconda\Library\mingw-w64\bin

    -------> System Variables <-------
    Installation_Path\Anaconda
    Installation_Path\Anaconda\Scripts
    Installation_Path\Anaconda\lib\bin
    Installation_Path\Anaconda\lib\usr\bin
    Installation_Path\Anaconda\python.exe

### Installing packages with conda:
If you already have a Python environment set up, and you are using the ``conda`` package manager,
you can get all packages by running

1. If you wish to install this in the base environment without creating any new environments, then you use:

        conda env update -n base --file environment.yml

2. If you want to create a specific environment for the course then use:

        # change "YOUR_ENV_NAME" with the name you want "DON'T use empty spaces in the environment name" 
        conda env create -n YOUR_ENV_NAME -file environment.yml

3. If face any problem run the command bleow to install all the package I use on my PC (It will take some time). 

         conda env update -n base --file all.yml

    
### Installing packages with pip
If you **don't want to use Anaconda** and already have a Python environment and are using pip to install packages, you need to run

    pip install -r requirements.txt

---
## Table of Content
<table>
<thead>
    <tr>
    <th>Video</th>
    <th>File Used</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=xH3_xIZLoJA&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=2&t=1s" target="_blank">#00 Introduction</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/raw/master/Power%20Point/Computer%20Vision-intro.pptx">Introduction to CV Power Point</a>
        </td>
    </tr>
    <tr>
        <td>
         <a href="https://www.youtube.com/watch?v=4mplUpakmGw&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=3" target="_blank">#01 Installing Packages</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/environment.yml">environment.yml</a>,
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/all.yml">all.yml</a>,
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/requirements.txt">requirements.txt</a>   
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=1KnC64nC-oc&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=4" target="_blank">#02 Opening and Saving Images</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2302_opening_saving.py">#02_opening_saving.py</a>,
        <a href="https://gist.github.com/karimelgazar/13d7fc3f673defc7dc0cba7f7d3dd8a5">VS Code</a></td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=dnjZBcw764w&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=5&t=0s" target="_blank">#03 Image Basics</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/illustration/show_pixels.py">show_pixels.py</a>,
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/illustration/mix_colors.py">mix_colors.py</a></td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=sxY0EXtBxAM&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=6&t=1s" target="_blank">#04 Drawing Shapes</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2304_drawing_shapes.py">#04_drawing_shapes.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=VOItbe13c8k&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=6&t=1s" target="_blank">#04.1 Using The Mouse</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2304_mouse.py">#04_mouse.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=TwgHMWt4Q44&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=7&t=0s" target="_blank">#05 Image Tranformations</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2305_img_tranformation.py">#05_img_tranformation.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=FzHBcychVq0&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=8&t=0s" target="_blank">#06 Image Arithmetic</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2306_img_arithmetic.py">#06_img_arithmetic.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=2tb50ILgQkY&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=9&t=0s" target="_blank">#07 Bitwise Operations</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2307_bitwise_operations.py">#07_bitwise_operations.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=3phdreDx17Q&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=10&t=0s" target="_blank">#08 Masking</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2308_masking.py">#08_masking.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=SqHfjeWkoVw&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=11&t=0s" target="_blank">#09 Splitting and Merging Channels</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2309_splitting_merging.py">#09_splitting_merging.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=HMCivIDUd-I&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=12&t=0s" target="_blank">#10 Color Spaces</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2310_color_spaces.py">#10_color_spaces.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=cWwpniPYpCs&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=13&t=0s" target="_blank">#11 Text and Trackbar</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2311_text_trackbar.py">#11_text_trackbar.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=ge4QuZKHpMM&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=14&t=0s" target="_blank">#12 Application on Text and Trackbar</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2312_face_recognition.py">#12_face_recognition.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=vVZbc9RhFsA&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=15&t=0s" target="_blank">#13 Histogram</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2313_histogram.py">#13_histogram.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=jCXApg0KDps&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=16&t=0s" target="_blank">#14 Blurring Part #01</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2314_blurring.py">#14_blurring.py</a>,
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/illustration/avg_blur_00.gif">avg_blur_00.gif</a>,
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/illustration/avg_blur_01.gif">avg_blur_01.gif</a>,
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/illustration/gauss.gif">gauss.gif</a>,
        <a href="https://medium.com/hackernoon/cv-for-busy-developers-convolutions-5c984f216e8c">Medium Article</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=b61A7mNMIX0&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=17&t=0s" target="_blank">#15 Blurring Part #02</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2314_blurring.py">#14_blurring.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=W5vRDwHFbmY&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=18&t=0s" target="_blank">#16 Thresholding Part #01</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2315_thresholding.py">#15_thresholding.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=DfH2XmHMgVQ&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=19&t=0s" target="_blank">#17 Thresholding Part #02</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2315_thresholding.py">#15_thresholding.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=hqrs6Ar6oDM&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=20&t=0s" target="_blank">#18 Edge Detection</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2316_find_edges.py">#16_find_edges.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=TYvZYSlkGH4&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=20&t=0s" target="_blank">#19 Extract Coins</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2317_extract_coins.py">#17_extract_coins.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=jQQ7QfYnRJE&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z&index=20&t=0s" target="_blank">#20 HSV Color Space</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2318_extract_coins.py">#18_hsv.py</a>,
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/illustration\hsv%20VS%20rgb.jfif">hsv VS rgb.jfif</a>,
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/illustration\hsv.jfif">hsv.jfif</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=WUEygqRB6rA&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z" target="_blank">#21 CV2.waitKey()</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2319_waitKey.py">#19_waitKey.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=1dWaUSTT1yE&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z" target="_blank">#22 Fonts</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2320_fonts.py">#20_fonts.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=RYe-eNEXrtY&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z" target="_blank">#23 Reading Videos</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2321_read_video.py">#21_read_video.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=9L64AbCga1Q&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z" target="_blank">#24 Saving Videos</a></td>
        <td>
        <a href="https://github.com/karimelgazar/OpenCV-in-Arabic-for-Beginners/blob/master/%2322_write_video.py">#22_write_video.py</a>
        </td>
    </tr>
    <tr>
        <td>
        <a href="https://www.youtube.com/watch?v=dri94iI0rf0&list=PLO1D3YWS7ep3Pfjls3LjBtp5XdvGpBD6Z" target="_blank">#25 Congratulation 💪 What's Next?</a></td>
        <td>---</td>
    </tr>
      
</tbody>
</table>
