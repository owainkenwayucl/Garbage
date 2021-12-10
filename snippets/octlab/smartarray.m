% Allocate arrays to GPUs *if* available.

function a = smartarray(data)
	if ((gpuDeviceCount()) > 0)
		a = gpuArray(data);
	else
		a = data;
	end
end

