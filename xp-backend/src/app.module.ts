import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ExperimentModule } from './modules/experiment/experiment.module';
import { ObservationModule } from './modules/observation/observation.module';
import { AuthModule } from './modules/auth/auth.module';
import { ProtectedModule } from './modules/protected/protected.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { getPostgresConfig } from './config/modules-configs/getPostgresConfig';
// import { getRedisConfig } from './config/modules-configs/getRedisConfig';
// import { RedisModule } from '@liaoliaots/nestjs-redis';
import { ConfigModule } from '@nestjs/config';
import { UserModule } from './modules/user/user.module';
import postgresConfig from './config/postgres.config';
import redisConfig from './config/redis.config';
import secretsConfig from './config/secrets.config';
import globalConfig from './config/global.config';

@Module({
  imports: [
    TypeOrmModule.forRootAsync(getPostgresConfig()),
    // RedisModule.forRootAsync(getRedisConfig()), // TODO use if necessary
    ConfigModule.forRoot({
      isGlobal: true,
      load: [postgresConfig, redisConfig, secretsConfig, globalConfig],
      ignoreEnvFile: false,
      envFilePath: ['config/.env'],
      cache: true,
    }),
    ExperimentModule,
    ObservationModule,
    AuthModule,
    ProtectedModule,
    UserModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
