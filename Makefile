.PHONY: all
all: controller_holder.stl keyboard_bottom.stl keyboard_top.stl switch_holder.stl

.PHONY: build
build:
	python minego.py

controller_holder.stl: build

keyboard_bottom.stl: build

keyboard_top.stl: build

switch_holder.stl: build

.PHONY: clean
clean:
	rm *.stl || true


