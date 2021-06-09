import argparse

from vietocr.model.trainer import Trainer
from vietocr.tool.config import Cfg

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True, help='see example at ')
    parser.add_argument('--checkpoint', required=False, help='your checkpoint')
    parser.add_argument('--pretrained', required=False, help='using pretrained')

    args = parser.parse_args()
    config = Cfg.load_config_from_file(args.config)

    # #
    # print(config)

    # while True:
    #     pass
    #

    trainer = Trainer(config)

    if args.checkpoint:
        print("Trong===============")
        trainer.load_checkpoint(args.checkpoint)
    print("Ngoai===============")
    #
    while True:
        pass
    #
    trainer.train()

if __name__ == '__main__':
    main()
