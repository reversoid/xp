import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { NextFunction, Request, Response } from 'express';
import { ValidationPipe } from '@nestjs/common';

/** Must be a middleware that transformes API-KEY and userId to jwt auth token because of tg bot */
const testMiddleware = async (
  req: Request,
  res: Response,
  next: NextFunction,
) => {
  const v = await new Promise((r) => setTimeout(() => r('completed'), 5000));
  console.log(v);

  next();
};

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalPipes(new ValidationPipe({ transform: true, whitelist: true }));
  app.use(testMiddleware);
  await app.listen(3000);
}
bootstrap();
