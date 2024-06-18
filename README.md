# Steel-Ball-Run-Detection-and-Analysis

Have you ever wanted to track a series of balls in a 2D plane in order to extract data off of them in an ultra-specific use case program? Well now you can with a Physics major's feeble attempts to code such a device! 

# How does it work? 

To be honest, I don't quite know. I am not a CS major, so its really just a bit of magic and a dash of hope. Respect that you give it a video and it gives you data, and all will be well with the world.

But actually it applies a few masks on every frame and detects balls, as well as predicts where they go and uses a reference to convert the changes of position in the balls as velocities, accelerations, and magnetic forces between the  balls.
from there a digital version of the balls is created, with each ball as its own object and set of data that can be looked at individually.