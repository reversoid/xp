import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ExperimentModule } from './modules/experiment/experiment.module';
import { ObservationModule } from './modules/observation/observation.module';
import { AuthModule } from './modules/auth/auth.module';
import { ProtectedModule } from './modules/protected/protected.module';

@Module({
  imports: [ExperimentModule, ObservationModule, AuthModule, ProtectedModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
