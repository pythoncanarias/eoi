#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fire

def hola(name="Mundo"):
    return f"Hola, {name}!"

if __name__ == '__main__':
    fire.Fire()
