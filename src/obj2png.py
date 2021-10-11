# -*- coding: utf-8 -*-

import ObjFile
import sys
import os
import glob

if __name__ == '__main__':

    class Args:
        def __init__(self):
            self.objfiles = ["oculos.obj"]
            self.quality = None
            # self.azim = 0.0  # 顺逆时针旋转，数值越大，逆时针旋转角度越大。 方位角/偏振角。
            # self.elevation = 0.0  # 上下旋转，数值越大，向上旋转角度越大。 倾斜角/仰角。  数值表示角度。

            # 正面
            self.azim = -90.0
            self.elevation = 90.0

            # 上下倾斜
            # self.azim = -90.0
            # self.elevation = 135.0
            # self.azim = -90.0
            # self.elevation = 65.0

            # 左右摇晃
            # self.azim = -70.0
            # self.elevation = 90.0
            # self.azim = -110.0
            # self.elevation = 90.0
            self.azim = -102.0
            self.elevation = 90.0

            self.scale = None
            self.animate = False
            self.outfile = None
            # self.outfile = "glass_left.png"
            self.view = True

    args = Args()

    objfiles = args.objfiles
    # 如果是通配符，使用glob查找
    if '*' in objfiles[0]:
        objfiles = glob.glob(objfiles[0])
    
    res = {'HIGH': 1200, 'MEDIUM': 600, 'LOW': 300}
    dpi = None
    # 设置quality
    if args.quality:
        if type(args.quality) == int:
            dpi = args.quality
        elif args.quality.upper() in res:
            dpi = res[args.quality.upper()]

    azim = None
    if args.azim is not None:
        azim = args.azim

    elevation = None
    if args.elevation is not None:
        elevation = args.elevation

    scale = None
    if args.scale:
        scale = args.scale

    animate = None
    if args.animate:
        animate = args.animate
        
    for objfile in objfiles:
        
        if os.path.isfile(objfile) and '.obj' in objfile:
            outfile = objfile.replace('.obj', '.png')
            if args.outfile:
                outfile = args.outfile
            if args.view:
                outfile = None
            else:
                print('Converting %s to %s' % (objfile, outfile))
            ob = ObjFile.ObjFile(objfile)
            ob.Plot(outfile, elevation=elevation, azim=azim, dpi=dpi, scale=scale, animate=animate)
        else:
            print('File %s not found or not file type .obj' % objfile)
            sys.exit(1)
