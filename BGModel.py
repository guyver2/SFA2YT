import numpy as np

# statistical background model, build a model from previous frames
class BGmodel(object):
    def __init__(self, size, shape):
        self.size = size #number of frame used to compute a model
        self.hist = np.zeros((self.size,shape[0],shape[1]), dtype=np.uint8)
        self.model = np.zeros((shape[0],shape[1]), dtype=np.uint8)
        self.cpt = 0
        self.ready = False

    # add a frame and update the model
    def add(self, frame, updateModel = True):
        self.hist[self.cpt,:,:] = np.copy(frame)
        self.cpt += 1
        if self.cpt == (self.size - 1) :
            self.ready = True
        self.cpt %= self.size
        if updateModel:
            self.updateModel()
    
    # update the model from the current frame history
    def updateModel(self):
        # np.mean is faster but median yields better results
        self.model = np.median(self.hist, axis=0).astype(np.uint8)
    
    def getModel(self):
        return np.copy(self.model)
       
    # substract the background to the current frame
    def apply(self, frame):
        # *2 to enhance the contrast
        res = 2*(np.abs(frame.astype(np.int32)-self.model.astype(np.int32)).astype(np.int32))
        res = np.clip(res, 0, 255)
        return res.astype(np.uint8)
