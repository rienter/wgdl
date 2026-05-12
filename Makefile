all: wgdl

wgdl: wgdl.py
	python3 -m venv . && \
		source ./bin/activate && \
		python3 -m pip install -r requirements.txt && \
		python3 -m pip install pyinstaller && \
		pyinstaller --onefile wgdl.py && \
		cp ./dist/wgdl* ./

clean:
	rm -rf bin build dist include lib lib64
