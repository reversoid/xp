import { Module } from '@nestjs/common';
import { FeedController } from './feed.controller';
import { FeedService } from './feed.service';
import { ExperimentModule } from '../experiment/experiment.module';

@Module({
  controllers: [FeedController],
  providers: [FeedService],
  imports: [ExperimentModule],
})
export class FeedModule {}
