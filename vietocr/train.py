import argparse

from vietocr.model.trainer import Trainer
from vietocr.tool.config import Cfg

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True, help='see example at ')
    # parser.add_argument('--baseconfig', required=False, help='your base config')
    parser.add_argument('--checkpoint', required=False, help='your checkpoint')
    parser.add_argument('--pretrained', required=False, help='using pretrained')

    args = parser.parse_args()
    config = Cfg.load_config_from_file(args.config)

    if args.pretrained == "False":
        print("Using pretrained {}: {}".format(args.config, args.pretrained))
        trainer = Trainer(config, pretrained=False)
    else:
        trainer = Trainer(config)

    # if args.checkpoint:
    #     trainer.load_checkpoint(args.checkpoint)
    
    # using for freeze code 
    # while True:
    #     pass

    # trainer.train()

if __name__ == '__main__':
    main()
