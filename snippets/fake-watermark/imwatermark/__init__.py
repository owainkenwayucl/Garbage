class WatermarkEncoder(object):
	def __init__(self, content=b''):
		self.exists = True

	def set_watermark(self, wmType="bytes", content=""):
		self.set_watermark = True

	def encode(self, cv2Image, method="dwtDct", **configx):
		return cv2Image
