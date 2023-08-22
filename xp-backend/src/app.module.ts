import { Module } from '@nestjs/common';
import { ExperimentModule } from './modules/experiment/experiment.module';
import { ObservationModule } from './modules/observation/observation.module';
import { AuthModule } from './modules/auth/auth.module';
import { ProtectedModule } from './modules/protected/protected.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { getPostgresConfig } from './config/modules-configs/getPostgresConfig';
import { ConfigModule } from '@nestjs/config';
import { UserModule } from './modules/user/user.module';
import postgresConfig from './config/postgres.config';
import secretsConfig from './config/secrets.config';
import globalConfig from './config/global.config';
import { TaskModule } from './modules/task/task.module';
import { ProfileModule } from './modules/profile/profile.module';
import { FeedModule } from './modules/feed/feed.module';

@Module({
  imports: [
    TypeOrmModule.forRootAsync(getPostgresConfig()),
    ConfigModule.forRoot({
      isGlobal: true,
      load: [postgresConfig, secretsConfig, globalConfig],
      ignoreEnvFile: false,
      envFilePath: ['config/.env'],
      cache: true,
    }),
    UserModule,
    ProfileModule,
    ExperimentModule,
    ObservationModule,
    AuthModule,
    ProtectedModule,
    TaskModule,
    FeedModule,
  ],
})
export class AppModule {}
