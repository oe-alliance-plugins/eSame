from setuptools import setup
import setup_translate

pkg = 'Extensions.eSame'
setup(name='enigma2-plugin-extensions-esame',
       version='3.0',
       description='eSame game for enigma2',
       package_dir={pkg: 'eSame'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'data/*.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
