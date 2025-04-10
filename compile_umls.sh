#!/bin/bash

plantuml -tsvg ./figs/uml/*.puml

git add ./figs/uml/*.puml

ls ./figs/uml/*.svg
