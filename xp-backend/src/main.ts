import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { NextFunction, Request, Response } from 'express';
import { ValidationPipe } from '@nestjs/common';
import { ProtectedService } from './modules/protected/protected.service';

/** A middleware that transformes secret_key and tg_user_id to jwt auth token */
const tgBotMiddlewareBuilder =
  (service: ProtectedService) =>
  async (req: Request, res: Response, next: NextFunction) => {
    const tg_user_id = req.headers['tg_user_id'] as string;
    const secret_key = req.headers['secret_key'] as string;
    if (tg_user_id === undefined || secret_key === undefined) {
      return next();
    }
    try {
      const tokens = await service.getTokensByTgUserId(
        Number(tg_user_id),
        secret_key,
      );
      req.headers['authorization'] = `Bearer ${tokens.access_token}`;
    } finally {
      next();
    }
  };

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  const protectedService = app.get(ProtectedService);

  app.useGlobalPipes(new ValidationPipe({ transform: true, whitelist: true }));
  app.use(tgBotMiddlewareBuilder(protectedService));
  await app.listen(3000);
}
bootstrap();
