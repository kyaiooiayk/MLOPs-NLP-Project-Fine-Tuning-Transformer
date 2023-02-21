import torch
import os
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint
from pytorch_lightning.callbacks.early_stopping import EarlyStopping

from data import DataModule
from model import ColaModel


def main():
    model = "google/bert_uncased_L-2_H-128_A-2"
    batch_size = 256
    # Automatically get the max nu of cpus available
    no_cpu = os.cpu_count()
    cola_data = DataModule(model, batch_size, no_cpu)
    cola_model = ColaModel()

    # To save model cjeckpoint
    checkpoint_callback = ModelCheckpoint(
        dirpath="./models", monitor="val_loss", mode="min"
    )

    # Early stopping helps the model not to overfit by mointoring val_loss in this case
    early_stopping_callback = EarlyStopping(
        monitor="val_loss", patience=3, verbose=True, mode="min"
    )

    tb_logger = pl.loggers.TensorBoardLogger("logs/", name="cola", version=1)
    trainer = pl.Trainer(
        default_root_dir="logs",
        gpus=(1 if torch.cuda.is_available() else 0),
        # To speed up the computation we could reduce this to 1
        max_epochs=3,
        # if Trueenabling fast_dev_run=True, will run one batch of training step and one batch of validation
        fast_dev_run=False,
        logger=tb_logger,
        callbacks=[checkpoint_callback, early_stopping_callback],
        log_every_n_steps=1,
        # If you have to resume training fromo the last one check points saved
        resume_from_checkpoint="./models/epoch=0-step=34.ckpt",
    )

    trainer.fit(cola_model, cola_data)


if __name__ == "__main__":
    # https://stackoverflow.com/questions/62691279/how-to-disable-tokenizers-parallelism-true-false-warning
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    main()
